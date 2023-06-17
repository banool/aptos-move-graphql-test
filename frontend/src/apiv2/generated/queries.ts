import * as Types from "./operations";

import { GraphQLClient } from "graphql-request";
import * as Dom from "graphql-request/dist/types.dom";

export const GetAccountResource = `
    query getAccountResource($address: String!, $resourceType: String!) {
  resource(address: $address, resourceType: $resourceType) {
    jsonDataV1
  }
}
    `;

export type SdkFunctionWrapper = <T>(
  action: (requestHeaders?: Record<string, string>) => Promise<T>,
  operationName: string,
  operationType?: string,
) => Promise<T>;

const defaultWrapper: SdkFunctionWrapper = (
  action,
  _operationName,
  _operationType,
) => action();

export function getSdk(
  client: GraphQLClient,
  withWrapper: SdkFunctionWrapper = defaultWrapper,
) {
  return {
    getAccountResource(
      variables: Types.GetAccountResourceQueryVariables,
      requestHeaders?: Dom.RequestInit["headers"],
    ): Promise<Types.GetAccountResourceQuery> {
      return withWrapper(
        (wrappedRequestHeaders) =>
          client.request<Types.GetAccountResourceQuery>(
            GetAccountResource,
            variables,
            { ...requestHeaders, ...wrappedRequestHeaders },
          ),
        "getAccountResource",
        "query",
      );
    },
  };
}
export type Sdk = ReturnType<typeof getSdk>;
