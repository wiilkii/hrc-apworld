from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import HorseRidingClassicWorld

def create_and_connect_regions(world: HorseRidingClassicWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: HorseRidingClassicWorld) -> None:
    forest = Region("Forest", world.player, world.multiworld)
    desert = Region("Desert", world.player, world.multiworld)
    city = Region("City", world.player, world.multiworld)
    farm = Region("Farm", world.player, world.multiworld)
    glue = Region("Glue", world.player, world.multiworld)

    regions = [forest, desert, city, farm, glue]

    # no region options

    world.multiworld.regions += regions

def connect_regions(world: HorseRidingClassicWorld) -> None:

    forest = world.multiworld.get_region("Forest", world.player)
    desert = world.multiworld.get_region("Desert", world.player)
    city = world.multiworld.get_region("City", world.player)
    farm = world.multiworld.get_region("Farm", world.player)
    glue = world.multiworld.get_region("Glue", world.player)

    forest.connect(desert, "Forest to Desert")
    desert.connect(city, "Desert to City")
    city.connect(farm, "City to Farm")
    farm.connect(city, "Farm to City")
    forest.connect(farm, "Forest to Farm")
    city.connect(glue, "City to Glue")
    farm.connect(glue, "Farm to Glue")

    # is this right?

    # no world options yet