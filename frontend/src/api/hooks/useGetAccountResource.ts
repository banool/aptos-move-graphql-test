import { Types } from "aptos";
import { UseQueryResult, useQuery } from "react-query";
import { getAccountResource } from "..";
import { ResponseError } from "../client";
import { useGlobalState } from "../../GlobalState";

export function useGetAccountResource(
  address: string,
  resource: string,
  options: {
    enabled?: boolean;
    // If you want to refetch the query when some additional criteria changes,
    // pass those criteria here. The query will be refetched when the value of
    // the state value given as additionalQueryCriteria changes.
    additionalQueryCriteria?: any;
  } = {},
): UseQueryResult<Types.MoveResource, ResponseError> {
  const [state, _setState] = useGlobalState();

  return useQuery<Types.MoveResource, ResponseError>(
    [
      "accountResource",
      { address },
      state.network_value,
      options.additionalQueryCriteria,
    ],
    () =>
      getAccountResource(
        { address, resourceType: resource },
        state.network_value,
      ),
    {
      refetchOnWindowFocus: false,
      enabled: options.enabled,
    },
  );
}
