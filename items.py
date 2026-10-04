from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import HorseRidingClassicWorld



ITEM_NAME_TO_ID = {
    "ProgressiveBreed": 1,
    "FarmKey": 2,
    "DesertKey": 3,
    "CityKey": 4,
    "GlueKey": 5,
    "Golden Apple": 6,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "ProgressiveBreed": ItemClassification.useful | ItemClassification.filler,
    "FarmKey": ItemClassification.progression,
    "DesertKey": ItemClassification.progression,
    "CityKey": ItemClassification.progression,
    "GlueKey": ItemClassification.progression,
    "Golden Apple": ItemClassification.progression,
}

class HorseRidingClassicItem(Item):
    game = "Horse Riding Classic"

def get_random_filler_item_name(world: HorseRidingClassicWorld) -> str:
    return "ProgressiveBreed"

def create_item_with_correct_classification(world: HorseRidingClassicWorld, name: str) -> HorseRidingClassicItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return HorseRidingClassicItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: HorseRidingClassicWorld) -> None:
    itempool: list[Item] = [
        world.create_item("ProgressiveBreed"),
        world.create_item("FarmKey"),
        world.create_item("DesertKey"),
        world.create_item("CityKey"),
        world.create_item("GlueKey")
    ]

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    # no precollected items

# https://github.com/ArchipelagoMW/Archipelago/blob/main/worlds/apquest/items.py