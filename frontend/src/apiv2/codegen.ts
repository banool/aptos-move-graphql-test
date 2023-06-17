import type { CodegenConfig } from "@graphql-codegen/cli";

const config: CodegenConfig = {
  overwrite: true,
  schema: "http://127.0.0.1:8080/v2",
  documents: "src/apiv2/queries/**/*.graphql",
  generates: {
    "src/apiv2/generated/types.ts": {
      config: {
        emitLegacyCommonJSImports: false,
        avoidOptionals: true,
      },
      plugins: ["typescript"],
    },
    "src/apiv2/generated/operations.ts": {
      preset: "import-types-preset",
      presetConfig: {
        typesPath: "./types",
      },
      plugins: ["typescript-operations"],
    },
    "src/apiv2/generated/queries.ts": {
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
