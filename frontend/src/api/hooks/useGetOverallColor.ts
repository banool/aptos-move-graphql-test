import { Types } from "aptos";
import { UseQueryResult, useQuery } from "react-query";
import { getOverallColor } from "..";
import { ResponseError } from "../client";
import { useGlobalState } from "../../GlobalState";
import { GetAccountResourceQuery } from "../../apiv2/generated/operations";
import { _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Color } from "../../food/generated/types";

export type useGetAccountResourceResponse = {
  accountResource: Types.MoveResource | undefined;
  isLoading: boolean;
  error: ResponseError | null;
};

export function useGetOverallColor(
  moduleAddress: string,
  mealAddress: string,
  options: {
    enabled?: boolean;
    // If you want to refetch the query when some additional criteria changes,
    // pass those criteria here. The query will be refetched when the value of
    // the state value given as additionalQueryCriteria changes.
    additionalQueryCriteria?: any;
  } = {},
): UseQueryResult<_0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Color> {
  const [state, _setState] = useGlobalState();

  return useQuery<
    _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Color,
    ResponseError
  >(
    [
      "overallColor",
      { moduleAddress, mealAddress },
      state.network_value,
      options.additionalQueryCriteria,
    ],
    () =>
      getOverallColor(
        moduleAddress,
        mealAddress,
        // We hit the v1 API for this.
        state.network_value,
      ),
    {
      refetchOnWindowFocus: false,
      enabled: options.enabled,
    },
  );
}
