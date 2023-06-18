import {
  Box,
  Flex,
  Text,
  FormControl,
  FormLabel,
  Input,
  Heading,
  Divider,
  Tr,
  Td,
  TableContainer,
  TableCaption,
  Table,
  Thead,
  Tbody,
  Th,
} from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import { useGetAccountResource } from "../../api/hooks/useGetAccountResource";
import {
  _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Meal,
  _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__MealStore,
  _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Protein,
  _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Vegetable,
  _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Color,
  _0x1__simple_map__SimpleMap,
  _0x1__simple_map__Element,
} from "../../food/generated/types";
import { useGetOverallColor } from "../../api/hooks/useGetOverallColor";

export const HomePage = () => {
  const {
    register,
    getValues,
    formState: { isValid },
  } = useForm();

  // Fetch the MealStore.
  const {
    data: mealStoreData,
    isLoading: mealStoreIsLoading,
    error: mealStoreError,
  } = useGetAccountResource(
    getValues("account_address"),
    `${getValues("module_address")}::food01::MealStore`,
    { enabled: isValid },
  );

  const mealStore:
    | _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__MealStore
    | undefined = mealStoreData ? mealStoreData.resource.jsonDataV1 : undefined;

  const mealStoreIndex = getValues("meal_store_index") || 0;
  const mealAddress = mealStore?.meals[mealStoreIndex].inner;

  const myForm = (
    <form>
      <FormControl>
        <FormLabel paddingTop={3} htmlFor="module_address">
          Module address
        </FormLabel>
        <Input
          id="module_address"
          placeholder="The account that contains the module."
          {...register("module_address", {
            required: "Must specify module address",
            minLength: { value: 2, message: "Minimum length should be 2" },
          })}
        />
      </FormControl>
      <FormControl>
        <FormLabel paddingTop={3} htmlFor="account_address">
          Account address
        </FormLabel>
        <Input
          id="account_address"
          placeholder="The account that contains the MealStore."
          {...register("account_address", {
            required: "Must specify account address",
            minLength: { value: 2, message: "Minimum length should be 2" },
          })}
        />
      </FormControl>
      <FormControl>
        <FormLabel paddingTop={3} htmlFor="meal_store_index">
          MealStore index
        </FormLabel>
        <Input
          id="meal_store_index"
          placeholder="Select a partical Meal in the MealStore. If not given we fetch the zeroth Meal."
          {...register("meal_store_index")}
        />
      </FormControl>
    </form>
  );

  const leftSection = myForm;
  let rightSection;

  if (mealStoreIsLoading) {
    rightSection = <Text>Loading MealStore data...</Text>;
  } else if (mealStoreError) {
    rightSection = (
      <Text>{`Failed to fetch MealStore: ${JSON.stringify(
        mealStoreError,
      )}`}</Text>
    );
  } else if (mealAddress) {
    let mealComponent = (
      <MealDisplay
        mealAddress={mealAddress}
        moduleAddress={getValues("module_address")}
      />
    );
    rightSection = (
      <Box>
        <Heading size="md" p={3}>
          Meal Data
        </Heading>
        {mealComponent}
      </Box>
    );
  }

  return (
    <Flex flex="1">
      <Box flex="8" p={5} borderRight="1px">
        {leftSection}
      </Box>
      <Box flex="9">
        <Box p={5}>{rightSection}</Box>
      </Box>
    </Flex>
  );
};

// Fetch the Meal data and display it.
export const MealDisplay = ({
  mealAddress,
  moduleAddress,
}: {
  mealAddress: string | undefined;
  moduleAddress: string;
}) => {
  // Fetch the data for the Meal.
  const {
    data: mealData,
    isLoading: mealIsLoading,
    error: mealError,
  } = useGetAccountResource(mealAddress!, `${moduleAddress}::food01::Meal`, {
    enabled: mealAddress !== undefined,
  });

  const meal:
    | _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Meal
    | undefined = mealData ? mealData.resource.jsonDataV1 : undefined;

  // Also fetch the overall color of the Meal. This uses a view function under the hood.
  const {
    data: mealColorData,
    isLoading: mealColorIsLoading,
    error: mealColorError,
  } = useGetOverallColor(moduleAddress, mealAddress!, {
    enabled: meal !== undefined,
  });

  let colorComponent;
  if (mealColorIsLoading) {
    colorComponent = <Text>Loading overall color...</Text>;
  } else if (mealColorError) {
    colorComponent = (
      <Text>{`Failed to fetch overall color: ${JSON.stringify(
        mealColorError,
      )}`}</Text>
    );
  } else {
    colorComponent = <ColorDisplay color={mealColorData!} />;
  }

  let display;
  if (mealIsLoading) {
    display = <Text>Loading Meal data...</Text>;
  } else if (mealError) {
    display = (
      <Text>{`Failed to fetch Meal data: ${JSON.stringify(mealError)}`}</Text>
    );
  } else {
    // We don't handle the option case.
    const proteinAddress = meal!.protein!.inner;
    const vegetableAddresses = meal!.vegetables!.map((v) => v.inner);
    const vegetableComponents = vegetableAddresses.map((v) => (
      <VegetableDisplay vegetableAddress={v} moduleAddress={moduleAddress} />
    ));
    display = (
      <Box p={3}>
        <Text paddingBottom={3}>{`Name: ${meal!.name}`}</Text>
        <Text paddingBottom={3}>{`Object address: ${mealAddress}`}</Text>
        <Text paddingBottom={3}>{`Cost: $${meal!.cost_usd}`}</Text>
        <Heading paddingTop={3} paddingBottom={3} size="sm">
          Popularity by country
        </Heading>
        <PopularityDisplay popularity={meal!.popularity_by_country} />
        <Heading paddingTop={6} size="sm">
          Protein
        </Heading>
        <ProteinDisplay
          proteinAddress={proteinAddress}
          moduleAddress={moduleAddress}
        />
        <Heading paddingTop={6} size="sm">
          Vegetables
        </Heading>
        {vegetableComponents}
        <Heading paddingTop={5} paddingBottom={3} size="sm">
          Overall color
        </Heading>
        <Text>
          The overall color of the meal when you take into account the colors of
          its ingredients.
        </Text>
        <Box paddingTop={3}>{colorComponent}</Box>
      </Box>
    );
  }

  return display;
};

// Fetch the protein data and display it.
export const ProteinDisplay = ({
  proteinAddress,
  moduleAddress,
}: {
  proteinAddress: string | undefined;
  moduleAddress: string;
}) => {
  const {
    data: proteinData,
    isLoading: proteinIsLoading,
    error: proteinError,
  } = useGetAccountResource(
    proteinAddress!,
    `${moduleAddress}::food01::Protein`,
    { enabled: proteinAddress !== undefined },
  );

  const protein:
    | _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Protein
    | undefined = proteinData ? proteinData.resource.jsonDataV1 : undefined;

  let display;
  if (proteinIsLoading) {
    display = <Text>Loading Protein data...</Text>;
  } else if (proteinError) {
    display = (
      <Text>{`Failed to fetch Protein data: ${JSON.stringify(
        proteinError,
      )}`}</Text>
    );
  } else {
    let color = protein!.aesthetic_profile.color;
    display = (
      <Box p={3}>
        <Text paddingBottom={3}>{`Name: ${protein!.name}`}</Text>
        <Text paddingBottom={3}>{`Energy: ${
          parseInt(protein!.energy_joules) / 1000
        } kJ`}</Text>
        <Text paddingBottom={3}>{`Texture: ${
          protein!.aesthetic_profile.texture
        }`}</Text>
        <Text paddingBottom={3}>Color</Text>
        <ColorDisplay color={color} />
      </Box>
    );
  }

  return display;
};

// TODO: Use the view function to get the overall color of the meal.

// Fetch the vegetable data and display it.
export const VegetableDisplay = ({
  vegetableAddress,
  moduleAddress,
}: {
  vegetableAddress: string | undefined;
  moduleAddress: string;
}) => {
  const {
    data: vegetableData,
    isLoading: vegetableIsLoading,
    error: vegetableError,
  } = useGetAccountResource(
    vegetableAddress!,
    `${moduleAddress}::food01::Vegetable`,
    { enabled: vegetableAddress !== undefined },
  );

  const vegetable:
    | _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Vegetable
    | undefined = vegetableData ? vegetableData.resource.jsonDataV1 : undefined;

  let display;
  if (vegetableIsLoading) {
    display = <Text>Loading Vegetable data...</Text>;
  } else if (vegetableError) {
    display = (
      <Text>{`Failed to fetch Vegetable data: ${JSON.stringify(
        vegetableError,
      )}`}</Text>
    );
  } else {
    let color = vegetable!.aesthetic_profile.color;
    display = (
      <Box p={3}>
        <Text paddingBottom={3}>{`Name: ${vegetable!.name}`}</Text>
        <Text paddingBottom={3}>{`Fibre: ${parseInt(
          vegetable!.fibre_grams,
        )} g`}</Text>
        <Text paddingBottom={3}>{`Energy: ${
          parseInt(vegetable!.energy_joules) / 1000
        } kJ`}</Text>
        <Text paddingBottom={3}>{`Texture: ${
          vegetable!.aesthetic_profile.texture
        }`}</Text>
        <Text paddingBottom={3}>Color</Text>
        <ColorDisplay color={color} />
      </Box>
    );
  }

  return display;
};

export const ColorDisplay = ({
  color,
}: {
  color: _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Color;
}) => {
  return (
    <Box bg={`rgba(${color.r}, ${color.g}, ${color.b}, 1)`} w={50} h={50} />
  );
};

// Display the popularity by country. As you can see, the keys and values in SimpleMaps
// just get resolved to `any` right now because we don't handle generics in the schema
// generator.
export const PopularityDisplay = ({
  popularity,
}: {
  popularity: _0x1__simple_map__SimpleMap;
}) => {
  let rows = [];
  for (var element of popularity.data) {
    rows.push(
      <Tr>
        <Td>{element.key}</Td>
        <Td>{`${element.value}%`}</Td>
      </Tr>,
    );
  }
  return (
    <TableContainer>
      <Table variant="simple">
        <Thead>
          <Tr>
            <Th>Country</Th>
            <Th>Popularity</Th>
          </Tr>
        </Thead>
        <Tbody>{rows}</Tbody>
      </Table>
    </TableContainer>
  );
};
