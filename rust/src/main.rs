mod generated;

use anyhow::{Context, Result};
use aptos_move_graphql_scalars::Address;
use aptos_sdk::rest_client::Client;
use clap::Parser;
use url::Url;

#[derive(Debug, Parser)]
pub struct Args {
    #[clap(long)]
    pub module_address: Address,

    #[clap(long)]
    pub account_address: Address,

    #[clap(long, default_value = "https://fullnode.devnet.aptoslabs.com")]
    pub rest_url: Url,
}

#[tokio::main]
async fn main() -> Result<()> {
    let args = Args::parse();

    let client = Client::new(args.rest_url);

    let resource_type = format!("{}::food01::MealStore", args.module_address.to_hex_literal());
    let response = client
        .get_resource::<generated::MealStore>(args.account_address, &resource_type)
        .await.context("Failed to get MealStore")?;

    let meal_object_address = response.into_inner().meals[0].inner;

    let resource_type = format!("{}::food01::Meal", args.module_address.to_hex_literal());
    let response = client
        .get_resource::<generated::Meal>(meal_object_address, &resource_type)
        .await.context("Failed to get MealStore")?;

    let meal = response.into_inner();

    // We get a nice typed representation of the resource.
    println!("Meal: {:#?}", meal);

    Ok(())
}
