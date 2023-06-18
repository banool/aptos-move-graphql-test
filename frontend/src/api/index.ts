import { AptosClient, Types } from "aptos";
import { withResponseError } from "./client";
import { _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Color } from "../food/generated/types";
import { Resource } from "../apiv2/generated/types";
import { getSdk } from "../apiv2/generated/queries";
import { GraphQLClient } from "graphql-request";
import { GetAccountResourceQuery } from "../apiv2/generated/operations";

export function getLedgerInfoWithoutResponseError(
  nodeUrl: string,
): Promise<Types.IndexResponse> {
  const client = new AptosClient(nodeUrl);
  return client.getLedgerInfo();
}

export function getAccountResource(
  requestParameters: {
    address: string;
    resourceType: string;
  },
  nodeUrl: string,
): Promise<GetAccountResourceQuery> {
  const innerClient = new GraphQLClient(nodeUrl);
  const client = getSdk(innerClient);
  return client.getAccountResource(requestParameters);
}

export async function getOverallColor(
  moduleId: string,
  mealAddress: string,
  nodeUrl: string,
): Promise<_0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Color> {
  const client = new AptosClient(nodeUrl);
  const payload: Types.ViewRequest = {
    function: `${moduleId}::food01::overall_color`,
    type_arguments: [],
    arguments: [mealAddress],
  };
  const response = await client.view(payload);
  return response[0] as _0x988449c911992da70870e7e322ec8715dc930815c818ab1124d3296427136509__food01__Color;
}
