from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as hrc_options


class HorseRidingClassicWorld(World):
    """
    Horse Riding Classic
    """

    game = "Horse Riding Classic"

    web = web_world.HorseRidingClassicWebWorld()

    options_dataclass = hrc_options.HorseRidingClassicOptions
    options: hrc_options.HorseRidingClassicOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Forest"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.HorseRidingClassicItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {"victory_item_id": items.ITEM_NAME_TO_ID["nom nom nom"]}