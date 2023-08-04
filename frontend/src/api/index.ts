import { AptosClient, Types } from "aptos";
import { withResponseError } from "./client";
import { Color } from "../food/generated/types";
import { GraphQLClient } from "graphql-request";

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
    ledgerVersion?: number;
  },
  nodeUrl: string,
): Promise<Types.MoveResource> {
  const client = new AptosClient(nodeUrl);
  const { address, resourceType, ledgerVersion } = requestParameters;
  let ledgerVersionBig;
  if (ledgerVersion !== undefined) {
    ledgerVersionBig = BigInt(ledgerVersion);
  }
  return withResponseError(
    client.getAccountResource(address, resourceType, {
      ledgerVersion: ledgerVersionBig,
    }),
  );
}

export async function getOverallColor(
  moduleId: string,
  mealAddress: string,
  nodeUrl: string,
): Promise<Color> {
  const client = new AptosClient(nodeUrl);
  const payload: Types.ViewRequest = {
    function: `${moduleId}::food01::overall_color`,
    type_arguments: [],
    arguments: [mealAddress],
  };
  const response = await client.view(payload);
  return response[0] as Color;
}
