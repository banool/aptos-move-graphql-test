import * as Types from "./types";

export type GetAccountResourceQueryVariables = Types.Exact<{
  address: Types.Scalars["String"];
  resourceType: Types.Scalars["String"];
}>;

export type GetAccountResourceQuery = {
  __typename?: "QueryRoot";
  resource: { __typename?: "Resource"; jsonDataV1: any };
};
