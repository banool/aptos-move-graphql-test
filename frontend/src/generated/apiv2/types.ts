export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = {
  [K in keyof T]: T[K];
};
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & {
  [SubKey in K]?: Maybe<T[SubKey]>;
};
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & {
  [SubKey in K]: Maybe<T[SubKey]>;
};
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  Address: any;
  JSON: any;
};

export type Module = {
  __typename?: "Module";
  moduleAbi: ModuleAbi;
};

export type ModuleAbi = {
  __typename?: "ModuleAbi";
  address: Scalars["Address"];
  name: Scalars["String"];
};

export type QueryRoot = {
  __typename?: "QueryRoot";
  modules: Array<Module>;
  resource: Resource;
};

export type QueryRootModulesArgs = {
  moduleIds: Array<Scalars["String"]>;
};

export type QueryRootResourceArgs = {
  address: Scalars["String"];
  resourceType: Scalars["String"];
};

export type Resource = {
  __typename?: "Resource";
  jsonDataV1: Scalars["JSON"];
};
