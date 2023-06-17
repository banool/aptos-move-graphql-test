import {
  Box,
  Flex,
  Text,
  FormControl,
  FormLabel,
  Input,
  Heading,
  Divider,
} from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import { useGetAccountResource } from "../../api/hooks/useGetAccountResource";
import {
  _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Meal,
  _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__MealStore,
  _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Protein,
  _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Vegetable,
} from "../../food/generated/types";

export const HomePage = () => {
  const {
    register,
    getValues,
    formState: { isValid },
  } = useForm();

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
        <Heading paddingTop={5} size="sm">
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
        <Box bg={`rgba(${color.r}, ${color.g}, ${color.b}, 1)`} w={50} h={50} />
      </Box>
    );
  }

  return display;
};

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
        <Box bg={`rgba(${color.r}, ${color.g}, ${color.b}, 1)`} w={50} h={50} />
      </Box>
    );
  }

  return display;
};
