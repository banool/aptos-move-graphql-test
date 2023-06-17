// Copyright (c) Daniel Porteous
// SPDX-License-Identifier: Apache-2.0

module addr::food01 {
    use std::option::{Self, Option};
    use std::signer;
    use std::string;
    use std::vector;
    use aptos_std::object::{Self, Object};
    use aptos_std::simple_map::{Self, SimpleMap};

    #[resource_group_member(group = aptos_framework::object::ObjectGroup)]
    struct Meal has key, store {
        /// The name of the meal.
        name: string::String,

        /// The protein in the meal.
        protein: Option<Object<Protein>>,

        /// The vegetables in the meal.
        vegetables: vector<Object<Vegetable>>,

        /// How much the meal costs in USD.
        cost_usd: u32,

        /// Popularity by country.
        popularity_by_country: SimpleMap<string::String, u32>,
    }

    #[resource_group_member(group = aptos_framework::object::ObjectGroup)]
    struct Protein has key, store {
        /// The name of the protein.
        name: string::String,

        /// How many joules of energy the protein has.
        energy_joules: u64,

        /// The aesthetic profile of the protein.
        aesthetic_profile: AestheticProfile,
    }

    #[resource_group_member(group = aptos_framework::object::ObjectGroup)]
    struct Vegetable has key, store {
        /// The name of the vegetable.
        name: string::String,

        /// How many joules of energy the vegetable has.
        energy_joules: u64,

        /// How many grams of fibre the vegetable has.
        fibre_grams: u64,

        /// The aesthetic profile of the vegetable.
        aesthetic_profile: AestheticProfile,
    }

    struct AestheticProfile has store {
        color: Color,
        texture: string::String,
    }

    struct Color has store {
        r: u8,
        g: u8,
        b: u8,
    }

    /// This goes on the account of the creator of meals so they have a reference to
    /// them. Normally I wouldn't do this and instead rely on emitting an event to
    /// determine what objects exist but in this example I don't have an indexer so
    /// this is easier.
    struct MealStore has key {
        meals: vector<Object<Meal>>
    }

    /// Create a new meal.
    public entry fun create(caller: &signer) acquires MealStore {
        let caller_addr = signer::address_of(caller);

        // Create the protein.
        let protein_ = Protein {
            name: string::utf8(b"Teriyaki Tofu"),
            energy_joules: 3529000,
            aesthetic_profile: AestheticProfile {
                color: Color {
                    r: 245,
                    g: 237,
                    b: 243,
                },
                texture: string::utf8(b"Smooth"),
            },
        };

        let constructor_ref = &object::create_object_from_account(caller);
        let object_signer = &object::generate_signer(constructor_ref);
        move_to(object_signer, protein_);
        let protein = object::object_from_constructor_ref(constructor_ref);

        // Create the potato.
        let potato_ = Vegetable {
            name: string::utf8(b"Potato"),
            energy_joules: 5220000,
            fibre_grams: 80,
            aesthetic_profile: AestheticProfile {
                color: Color {
                    r: 199,
                    g: 201,
                    b: 147,
                },
                texture: string::utf8(b"Buttery"),
            },
        };

        let constructor_ref = &object::create_object_from_account(caller);
        let object_signer = &object::generate_signer(constructor_ref);
        move_to(object_signer, potato_);
        let potato = object::object_from_constructor_ref(constructor_ref);

        // Create the carrot.
        let carrot_ = Vegetable {
            name: string::utf8(b"Carrot"),
            energy_joules: 1760000,
            fibre_grams: 100,
            aesthetic_profile: AestheticProfile {
                color: Color {
                    r: 255,
                    g: 165,
                    b: 0,
                },
                texture: string::utf8(b"Crunchy"),
            },
        };

        let constructor_ref = &object::create_object_from_account(caller);
        let object_signer = &object::generate_signer(constructor_ref);
        move_to(object_signer, carrot_);
        let carrot = object::object_from_constructor_ref(constructor_ref);

        // Create the meal.
        let vegetables = vector::empty();
        vector::push_back(&mut vegetables, potato);
        vector::push_back(&mut vegetables, carrot);

        let popularity_by_country = simple_map::create();
        simple_map::add(&mut popularity_by_country, string::utf8(b"USA"), 43);
        simple_map::add(&mut popularity_by_country, string::utf8(b"Australia"), 62);
        simple_map::add(&mut popularity_by_country, string::utf8(b"Japan"), 74);

        let meal_ = Meal {
            name: string::utf8(b"Teriyaki Tofu with Potato and Carrot"),
            protein: option::some(protein),
            vegetables,
            cost_usd: 10,
            popularity_by_country,
        };

        let constructor_ref = &object::create_object_from_account(caller);
        let object_signer = &object::generate_signer(constructor_ref);
        move_to(object_signer, meal_);
        let meal = object::object_from_constructor_ref(constructor_ref);

        // If there is no MealStore on the caller's account create one.
        if (!exists<MealStore>(caller_addr)) {
            let meal_store = MealStore {
                meals: vector::empty(),
            };
            move_to(caller, meal_store);
        };

        // Add the Meal to the MealStore.
        let meal_store = borrow_global_mut<MealStore>(caller_addr);
        vector::push_back(&mut meal_store.meals, meal);
    }

    #[view]
    fun overall_color(meal: Object<Meal>): Color acquires Meal, Protein, Vegetable {
        let meal_ = borrow_global<Meal>(object::object_address(&meal));

        let r: u64 = 0;
        let g: u64 = 0;
        let b: u64 = 0;
        let count: u64 = 0;

        let len = vector::length(&meal_.vegetables);
        let i = 0;
        while (i < len) {
            let vegetable = vector::borrow(&meal_.vegetables, i);
            let vegetable_ = borrow_global<Vegetable>(object::object_address(vegetable));
            r = r + (vegetable_.aesthetic_profile.color.r as u64);
            g = g + (vegetable_.aesthetic_profile.color.g as u64);
            b = b + (vegetable_.aesthetic_profile.color.b as u64);
            count = count + 1;
            i = i + 1;
        };

        if (option::is_some(&meal_.protein)) {
            let protein = option::borrow(&meal_.protein);
            let protein_ = borrow_global<Protein>(object::object_address(protein));
            r = r + (protein_.aesthetic_profile.color.r as u64);
            g = g + (protein_.aesthetic_profile.color.g as u64);
            b = b + (protein_.aesthetic_profile.color.b as u64);
            count = count + 1;
        };

        Color {
            r: ((r / count) as u8),
            g: ((g / count) as u8),
            b: ((b / count) as u8),
        }
    }
}
