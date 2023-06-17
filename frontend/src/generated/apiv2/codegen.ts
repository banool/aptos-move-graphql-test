import type { CodegenConfig } from "@graphql-codegen/cli";

const config: CodegenConfig = {
  overwrite: true,
  schema: "http://127.0.0.1:8080/v2",
  generates: {
    "src/generated/apiv2/types.ts": {
      config: {
        emitLegacyCommonJSImports: false,
        avoidOptionals: true,
      },
      plugins: ["typescript"],
    },
    "src/generated/apiv2/operations.ts": {
      preset: "import-types-preset",
      presetConfig: {
        typesPath: "./types",
      },
      plugins: ["typescript-operations"],
    },
    "src/generated/apiv2/queries.ts": {
      preset: "import-types-preset",
      presetConfig: {
        typesPath: "./operations",
      },
      plugins: ["typescript-graphql-request"],
      config: {
        documentMode: "string",
        documentVariableSuffix: "",
      },
    },
  },
};

export default config;
