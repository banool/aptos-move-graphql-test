import argparse
import asyncio
import json
import logging
from aptos_sdk.async_client import RestClient
from schema_types import MealStore, Meal


logging.basicConfig(level="INFO", format="%(asctime)s - %(levelname)s - %(message)s")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("--module-address", required=True)
    parser.add_argument("--account-address", required=True)
    parser.add_argument(
        "--rest-url", default="https://fullnode.devnet.aptoslabs.com/v1"
    )
    args = parser.parse_args()
    if not args.module_address.startswith("0x"):
        args.module_address = f"0x{args.module_address}"
    if not args.account_address.startswith("0x"):
        args.account_address = f"0x{args.account_address}"
    return args


async def main():
    args = parse_args()

    if args.debug:
        logging.setLevel("DEBUG")

    client = RestClient(args.rest_url)

    resource_type = f"{args.module_address}::food01::MealStore"
    response = await client.account_resource(args.account_address, resource_type)
    meal_store: MealStore = response["data"]

    meal_object_address = meal_store["meals"][0]["inner"]
    resource_type = f"{args.module_address}::food01::Meal"
    response = await client.account_resource(meal_object_address, resource_type)
    meal: Meal = response["data"]

    print(json.dumps(meal, indent=4))


if __name__ == "__main__":
    asyncio.run(main())
