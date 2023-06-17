import { Types } from "aptos";
import { UseQueryResult, useQuery } from "react-query";
import { getAccountResource } from "..";
import { ResponseError } from "../client";
import { useGlobalState } from "../../GlobalState";
import { GetAccountResourceQuery } from "../../apiv2/generated/operations";

export type useGetAccountResourceResponse = {
  accountResource: Types.MoveResource | undefined;
  isLoading: boolean;
  error: ResponseError | null;
};

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
): UseQueryResult<GetAccountResourceQuery> {
  const [state, _setState] = useGlobalState();

  return useQuery<GetAccountResourceQuery, ResponseError>(
    [
      "accountResource",
      { address },
      state.network_value,
      options.additionalQueryCriteria,
    ],
    () =>
      getAccountResource(
        { address, resourceType: resource },
        // We want to hit the GraphQL endpoint.
        `${state.network_value}/v2`,
      ),
    {
      refetchOnWindowFocus: false,
      enabled: options.enabled,
    },
  );
}
