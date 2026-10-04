from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items

import csv

if TYPE_CHECKING:
    from .world import HorseRidingClassicWorld

LOCATION_NAME_TO_ID = {
    "Starting Apple": 71,
    "High Fire Ring": 16,
    "Left Vertical Tube": 4,
    "Right Vertical Tube": 7,
    "High Horizontal Tube": 12,
    "Crystal Apple 1": 26,
    "Crystal Apple 2": 27,
    "Crystal Apple 3": 28,
    "Fairy Ring": 24,
    "Behind Waterfall": 18,
    "Fairy Ring Diagonal Tube": 3,
    "Horse Trap Box": 8,
    "Gem's Horse Race": 72,
    "Low Fire Ring": 21,
    "Horse Race Diagonal Tube": 15,
    "High Small Diagonal Tube": 20,
    "Cave Entrance": 29,
    "Bear Apple": 39,
    "West Floating Island": 45,
    "East Floating Island": 6,
    "Wizard Apple 1": 38,
    "Wizard Apple 2": 37,
    "Wizard Apple 3": 36,
    "Lone Apple (Nature Lover)": 1,
    "On The Rocks": 17,
    "Stuck Between an Apple and a Hard Place": 10,
    "Apple Casino 1": 30,
    "Apple Casino 2": 31,
    "Apple Casino 3": 32,
    "Tumbleweed": 83,
    "An Apple is an Egg Right? (Nest)": 2,
    "Is that a seagull? (Bird Apple) (Bitch Ass Bird = B.A.B.)": 84,
    "Arch Apple (i use arch btw)": 42,
    "On the Arch Apple": 44,
    "Old Old Town Entrance": 100,
    "Shoot Horseboy": 59,
    "Jail": 43,
    "Top of Saloon": 19,
    "Top of Cactus": 22,
    "Fire Ring": 13,
    "Cactus Ring": 5,
    "Wait I'm Goated (Daredevil)": 35,
    "Underground Island": 25,
    "In between a stelagmite and a stelagtite (i cant spell": 34,
    "Chuck's Apple": 47,
    "Canyon Ledge": 9,
    "Between the Rocks": 11,
    "Trench Apple (Towards the north)": 23,
    "South Trench": 14,
    "Gorge Runner": 33,
    "Crane": 60,
    "Crane Cockpit": 62,
    "Subway": 86,
    "Subway Bathroom": 67,
    "West Low H Building": 66,
    "East Low H Building": 63,
    "west High H Building": 64,
    "east High H Building": 65,
    "Sewer Pipe": 53,
    "City's Edge (SE)": 70,
    "SE In Between Buildings": 68,
    "That Fucking Bird That I Hate": 91,
    "Eat This Apple? Sign": 61,
    "Top of Building (North)": 90,
    "Ledge of Building (North)": 69,
    "Cardboard Building North": 87,
    "Cardboard Building South": 88,
    "Parking Garage 1": 55,
    "Parking Garage 2": 56,
    "Parking Garage 3": 57,
    "Top of Building South": 89,
    "Ledge (West)": 58,
    "Water Overlook Pier Bridge Thingy": 40,
    "Doctor Evil": 85,
    "With the Tractors": 76,
    "In the Tractor": 77,
    "UFO Apple 1": 74,
    "UFO Apple 2": 52,
    "UFO Apple 3": 73,
    "God?": 51,
    "Swing": 99,
    "Dog House": 54,
    "Top of Silo": 82,
    "Over the Tube": 94,
    "Southwest Corn": 81,
    "Tractor Race": 93,
    "UFO Corn": 79,
    "Silo Corn": 78,
    "Horse Fan Club 1": 48,
    "Horse Fan Club 2": 49,
    "Horse Fan Club 3": 50,
    "The Sacrifice": 46,
    "Top of Barn": 75,
    "Upper Barn Rafters": 96,
    "Lower Barn Rafters 1": 97,
    "Lower Barn Rafters 2": 98,
    "Dentist": 92,
    "Behind Barn": 95,
    "North Corn": 80,
    "Golden Apple": 999,
}

class HorispelagoClassicLocation(Location):
    game: str = "Horse Riding Classic"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: HorseRidingClassicWorld) -> None:
    create_regular_locations(world)
    # create_events(world)

def create_regular_locations(world: HorseRidingClassicWorld) -> None:
    forest = world.get_region("Forest")
    desert = world.get_region("Desert")
    city = world.get_region("City")
    farm = world.get_region("Farm")
    glue = world.get_region("Glue")

    # Forest
    starting_apple = HorispelagoClassicLocation(
        world.player, "Starting Apple", world.location_name_to_id["Starting Apple"], forest
    )
    forest.locations.append(starting_apple)

    high_fire_ring = HorispelagoClassicLocation(
        world.player, "High Fire Ring", world.location_name_to_id["High Fire Ring"], forest
    )
    forest.locations.append(high_fire_ring)

    left_vertical_tube = HorispelagoClassicLocation(
        world.player, "Left Vertical Tube", world.location_name_to_id["Left Vertical Tube"], forest
    )
    forest.locations.append(left_vertical_tube)

    right_vertical_tube = HorispelagoClassicLocation(
        world.player, "Right Vertical Tube", world.location_name_to_id["Right Vertical Tube"], forest
    )
    forest.locations.append(right_vertical_tube)

    high_horizontal_tube = HorispelagoClassicLocation(
        world.player, "High Horizontal Tube", world.location_name_to_id["High Horizontal Tube"], forest
    )
    forest.locations.append(high_horizontal_tube)

    crystal_apple_1 = HorispelagoClassicLocation(
        world.player, "Crystal Apple 1", world.location_name_to_id["Crystal Apple 1"], forest
    )
    forest.locations.append(crystal_apple_1)

    crystal_apple_2 = HorispelagoClassicLocation(
        world.player, "Crystal Apple 2", world.location_name_to_id["Crystal Apple 2"], forest
    )
    forest.locations.append(crystal_apple_2)

    crystal_apple_3 = HorispelagoClassicLocation(
        world.player, "Crystal Apple 3", world.location_name_to_id["Crystal Apple 3"], forest
    )
    forest.locations.append(crystal_apple_3)

    fairy_ring = HorispelagoClassicLocation(
        world.player, "Fairy Ring", world.location_name_to_id["Fairy Ring"], forest
    )
    forest.locations.append(fairy_ring)

    behind_waterfall = HorispelagoClassicLocation(
        world.player, "Behind Waterfall", world.location_name_to_id["Behind Waterfall"], forest
    )
    forest.locations.append(behind_waterfall)

    fairy_ring_diagonal_tube = HorispelagoClassicLocation(
        world.player, "Fairy Ring Diagonal Tube", world.location_name_to_id["Fairy Ring Diagonal Tube"], forest
    )
    forest.locations.append(fairy_ring_diagonal_tube)

    horse_trap_box = HorispelagoClassicLocation(
        world.player, "Horse Trap Box", world.location_name_to_id["Horse Trap Box"], forest
    )
    forest.locations.append(horse_trap_box)

    gem_s_horse_race = HorispelagoClassicLocation(
        world.player, "Gem's Horse Race", world.location_name_to_id["Gem's Horse Race"], forest
    )
    forest.locations.append(gem_s_horse_race)

    low_fire_ring = HorispelagoClassicLocation(
        world.player, "Low Fire Ring", world.location_name_to_id["Low Fire Ring"], forest
    )
    forest.locations.append(low_fire_ring)

    horse_race_diagonal_tube = HorispelagoClassicLocation(
        world.player, "Horse Race Diagonal Tube", world.location_name_to_id["Horse Race Diagonal Tube"], forest
    )
    forest.locations.append(horse_race_diagonal_tube)

    high_small_diagonal_tube = HorispelagoClassicLocation(
        world.player, "High Small Diagonal Tube", world.location_name_to_id["High Small Diagonal Tube"], forest
    )
    forest.locations.append(high_small_diagonal_tube)

    cave_entrance = HorispelagoClassicLocation(
        world.player, "Cave Entrance", world.location_name_to_id["Cave Entrance"], forest
    )
    forest.locations.append(cave_entrance)

    bear_apple = HorispelagoClassicLocation(
        world.player, "Bear Apple", world.location_name_to_id["Bear Apple"], forest
    )
    forest.locations.append(bear_apple)

    west_floating_island = HorispelagoClassicLocation(
        world.player, "West Floating Island", world.location_name_to_id["West Floating Island"], forest
    )
    forest.locations.append(west_floating_island)

    east_floating_island = HorispelagoClassicLocation(
        world.player, "East Floating Island", world.location_name_to_id["East Floating Island"], forest
    )
    forest.locations.append(east_floating_island)

    wizard_apple_1 = HorispelagoClassicLocation(
        world.player, "Wizard Apple 1", world.location_name_to_id["Wizard Apple 1"], forest
    )
    forest.locations.append(wizard_apple_1)

    wizard_apple_2 = HorispelagoClassicLocation(
        world.player, "Wizard Apple 2", world.location_name_to_id["Wizard Apple 2"], forest
    )
    forest.locations.append(wizard_apple_2)

    wizard_apple_3 = HorispelagoClassicLocation(
        world.player, "Wizard Apple 3", world.location_name_to_id["Wizard Apple 3"], forest
    )
    forest.locations.append(wizard_apple_3)

    lone_apple_nature_lover = HorispelagoClassicLocation(
        world.player, "Lone Apple (Nature Lover)", world.location_name_to_id["Lone Apple (Nature Lover)"], forest
    )
    forest.locations.append(lone_apple_nature_lover)

    on_the_rocks = HorispelagoClassicLocation(
        world.player, "On The Rocks", world.location_name_to_id["On The Rocks"], forest
    )
    forest.locations.append(on_the_rocks)


    # Desert
    stuck_between_an_apple_and_a_hard_place = HorispelagoClassicLocation(
        world.player, "Stuck Between an Apple and a Hard Place", world.location_name_to_id["Stuck Between an Apple and a Hard Place"], desert
    )
    desert.locations.append(stuck_between_an_apple_and_a_hard_place)

    apple_casino_1 = HorispelagoClassicLocation(
        world.player, "Apple Casino 1", world.location_name_to_id["Apple Casino 1"], desert
    )
    desert.locations.append(apple_casino_1)

    apple_casino_2 = HorispelagoClassicLocation(
        world.player, "Apple Casino 2", world.location_name_to_id["Apple Casino 2"], desert
    )
    desert.locations.append(apple_casino_2)

    apple_casino_3 = HorispelagoClassicLocation(
        world.player, "Apple Casino 3", world.location_name_to_id["Apple Casino 3"], desert
    )
    desert.locations.append(apple_casino_3)

    tumbleweed = HorispelagoClassicLocation(
        world.player, "Tumbleweed", world.location_name_to_id["Tumbleweed"], desert
    )
    desert.locations.append(tumbleweed)

    an_apple_is_an_egg_right_nest = HorispelagoClassicLocation(
        world.player, "An Apple is an Egg Right? (Nest)", world.location_name_to_id["An Apple is an Egg Right? (Nest)"], desert
    )
    desert.locations.append(an_apple_is_an_egg_right_nest)

    is_that_a_seagull_bird_apple_bitch_ass_bird_b_a_b = HorispelagoClassicLocation(
        world.player, "Is that a seagull? (Bird Apple) (Bitch Ass Bird = B.A.B.)", world.location_name_to_id["Is that a seagull? (Bird Apple) (Bitch Ass Bird = B.A.B.)"], desert
    )
    desert.locations.append(is_that_a_seagull_bird_apple_bitch_ass_bird_b_a_b)

    arch_apple_i_use_arch_btw = HorispelagoClassicLocation(
        world.player, "Arch Apple (i use arch btw)", world.location_name_to_id["Arch Apple (i use arch btw)"], desert
    )
    desert.locations.append(arch_apple_i_use_arch_btw)

    on_the_arch_apple = HorispelagoClassicLocation(
        world.player, "On the Arch Apple", world.location_name_to_id["On the Arch Apple"], desert
    )
    desert.locations.append(on_the_arch_apple)

    old_old_town_entrance = HorispelagoClassicLocation(
        world.player, "Old Old Town Entrance", world.location_name_to_id["Old Old Town Entrance"], desert
    )
    desert.locations.append(old_old_town_entrance)

    shoot_horseboy = HorispelagoClassicLocation(
        world.player, "Shoot Horseboy", world.location_name_to_id["Shoot Horseboy"], desert
    )
    desert.locations.append(shoot_horseboy)

    jail = HorispelagoClassicLocation(
        world.player, "Jail", world.location_name_to_id["Jail"], desert
    )
    desert.locations.append(jail)

    top_of_saloon = HorispelagoClassicLocation(
        world.player, "Top of Saloon", world.location_name_to_id["Top of Saloon"], desert
    )
    desert.locations.append(top_of_saloon)

    top_of_cactus = HorispelagoClassicLocation(
        world.player, "Top of Cactus", world.location_name_to_id["Top of Cactus"], desert
    )
    desert.locations.append(top_of_cactus)

    fire_ring = HorispelagoClassicLocation(
        world.player, "Fire Ring", world.location_name_to_id["Fire Ring"], desert
    )
    desert.locations.append(fire_ring)

    cactus_ring = HorispelagoClassicLocation(
        world.player, "Cactus Ring", world.location_name_to_id["Cactus Ring"], desert
    )
    desert.locations.append(cactus_ring)

    wait_i_m_goated_daredevil = HorispelagoClassicLocation(
        world.player, "Wait I'm Goated (Daredevil)", world.location_name_to_id["Wait I'm Goated (Daredevil)"], desert
    )
    desert.locations.append(wait_i_m_goated_daredevil)

    underground_island = HorispelagoClassicLocation(
        world.player, "Underground Island", world.location_name_to_id["Underground Island"], desert
    )
    desert.locations.append(underground_island)

    in_between_a_stelagmite_and_a_stelagtite_i_cant_spell = HorispelagoClassicLocation(
        world.player, "In between a stelagmite and a stelagtite (i cant spell", world.location_name_to_id["In between a stelagmite and a stelagtite (i cant spell"], desert
    )
    desert.locations.append(in_between_a_stelagmite_and_a_stelagtite_i_cant_spell)

    chuck_s_apple = HorispelagoClassicLocation(
        world.player, "Chuck's Apple", world.location_name_to_id["Chuck's Apple"], desert
    )
    desert.locations.append(chuck_s_apple)

    canyon_ledge = HorispelagoClassicLocation(
        world.player, "Canyon Ledge", world.location_name_to_id["Canyon Ledge"], desert
    )
    desert.locations.append(canyon_ledge)

    between_the_rocks = HorispelagoClassicLocation(
        world.player, "Between the Rocks", world.location_name_to_id["Between the Rocks"], desert
    )
    desert.locations.append(between_the_rocks)

    trench_apple_towards_the_north = HorispelagoClassicLocation(
        world.player, "Trench Apple (Towards the north)", world.location_name_to_id["Trench Apple (Towards the north)"], desert
    )
    desert.locations.append(trench_apple_towards_the_north)

    south_trench = HorispelagoClassicLocation(
        world.player, "South Trench", world.location_name_to_id["South Trench"], desert
    )
    desert.locations.append(south_trench)

    gorge_runner = HorispelagoClassicLocation(
        world.player, "Gorge Runner", world.location_name_to_id["Gorge Runner"], desert
    )
    desert.locations.append(gorge_runner)


    # City
    crane = HorispelagoClassicLocation(
        world.player, "Crane", world.location_name_to_id["Crane"], city
    )
    city.locations.append(crane)

    crane_cockpit = HorispelagoClassicLocation(
        world.player, "Crane Cockpit", world.location_name_to_id["Crane Cockpit"], city
    )
    city.locations.append(crane_cockpit)

    subway = HorispelagoClassicLocation(
        world.player, "Subway", world.location_name_to_id["Subway"], city
    )
    city.locations.append(subway)

    subway_bathroom = HorispelagoClassicLocation(
        world.player, "Subway Bathroom", world.location_name_to_id["Subway Bathroom"], city
    )
    city.locations.append(subway_bathroom)

    west_low_h_building = HorispelagoClassicLocation(
        world.player, "West Low H Building", world.location_name_to_id["West Low H Building"], city
    )
    city.locations.append(west_low_h_building)

    east_low_h_building = HorispelagoClassicLocation(
        world.player, "East Low H Building", world.location_name_to_id["East Low H Building"], city
    )
    city.locations.append(east_low_h_building)

    west_high_h_building = HorispelagoClassicLocation(
        world.player, "west High H Building", world.location_name_to_id["west High H Building"], city
    )
    city.locations.append(west_high_h_building)

    east_high_h_building = HorispelagoClassicLocation(
        world.player, "east High H Building", world.location_name_to_id["east High H Building"], city
    )
    city.locations.append(east_high_h_building)

    sewer_pipe = HorispelagoClassicLocation(
        world.player, "Sewer Pipe", world.location_name_to_id["Sewer Pipe"], city
    )
    city.locations.append(sewer_pipe)

    city_s_edge_se = HorispelagoClassicLocation(
        world.player, "City's Edge (SE)", world.location_name_to_id["City's Edge (SE)"], city
    )
    city.locations.append(city_s_edge_se)

    se_in_between_buildings = HorispelagoClassicLocation(
        world.player, "SE In Between Buildings", world.location_name_to_id["SE In Between Buildings"], city
    )
    city.locations.append(se_in_between_buildings)

    that_fucking_bird_that_i_hate = HorispelagoClassicLocation(
        world.player, "That Fucking Bird That I Hate", world.location_name_to_id["That Fucking Bird That I Hate"], city
    )
    city.locations.append(that_fucking_bird_that_i_hate)

    eat_this_apple_sign = HorispelagoClassicLocation(
        world.player, "Eat This Apple? Sign", world.location_name_to_id["Eat This Apple? Sign"], city
    )
    city.locations.append(eat_this_apple_sign)

    top_of_building_north = HorispelagoClassicLocation(
        world.player, "Top of Building (North)", world.location_name_to_id["Top of Building (North)"], city
    )
    city.locations.append(top_of_building_north)

    ledge_of_building_north = HorispelagoClassicLocation(
        world.player, "Ledge of Building (North)", world.location_name_to_id["Ledge of Building (North)"], city
    )
    city.locations.append(ledge_of_building_north)

    cardboard_building_north = HorispelagoClassicLocation(
        world.player, "Cardboard Building North", world.location_name_to_id["Cardboard Building North"], city
    )
    city.locations.append(cardboard_building_north)

    cardboard_building_south = HorispelagoClassicLocation(
        world.player, "Cardboard Building South", world.location_name_to_id["Cardboard Building South"], city
    )
    city.locations.append(cardboard_building_south)

    parking_garage_1 = HorispelagoClassicLocation(
        world.player, "Parking Garage 1", world.location_name_to_id["Parking Garage 1"], city
    )
    city.locations.append(parking_garage_1)

    parking_garage_2 = HorispelagoClassicLocation(
        world.player, "Parking Garage 2", world.location_name_to_id["Parking Garage 2"], city
    )
    city.locations.append(parking_garage_2)

    parking_garage_3 = HorispelagoClassicLocation(
        world.player, "Parking Garage 3", world.location_name_to_id["Parking Garage 3"], city
    )
    city.locations.append(parking_garage_3)

    top_of_building_south = HorispelagoClassicLocation(
        world.player, "Top of Building South", world.location_name_to_id["Top of Building South"], city
    )
    city.locations.append(top_of_building_south)

    ledge_west = HorispelagoClassicLocation(
        world.player, "Ledge (West)", world.location_name_to_id["Ledge (West)"], city
    )
    city.locations.append(ledge_west)

    water_overlook_pier_bridge_thingy = HorispelagoClassicLocation(
        world.player, "Water Overlook Pier Bridge Thingy", world.location_name_to_id["Water Overlook Pier Bridge Thingy"], city
    )
    city.locations.append(water_overlook_pier_bridge_thingy)

    doctor_evil = HorispelagoClassicLocation(
        world.player, "Doctor Evil", world.location_name_to_id["Doctor Evil"], city
    )
    city.locations.append(doctor_evil)


    # Farm
    with_the_tractors = HorispelagoClassicLocation(
        world.player, "With the Tractors", world.location_name_to_id["With the Tractors"], farm
    )
    farm.locations.append(with_the_tractors)

    in_the_tractor = HorispelagoClassicLocation(
        world.player, "In the Tractor", world.location_name_to_id["In the Tractor"], farm
    )
    farm.locations.append(in_the_tractor)

    ufo_apple_1 = HorispelagoClassicLocation(
        world.player, "UFO Apple 1", world.location_name_to_id["UFO Apple 1"], farm
    )
    farm.locations.append(ufo_apple_1)

    ufo_apple_2 = HorispelagoClassicLocation(
        world.player, "UFO Apple 2", world.location_name_to_id["UFO Apple 2"], farm
    )
    farm.locations.append(ufo_apple_2)

    ufo_apple_3 = HorispelagoClassicLocation(
        world.player, "UFO Apple 3", world.location_name_to_id["UFO Apple 3"], farm
    )
    farm.locations.append(ufo_apple_3)

    god = HorispelagoClassicLocation(
        world.player, "God?", world.location_name_to_id["God?"], farm
    )
    farm.locations.append(god)

    swing = HorispelagoClassicLocation(
        world.player, "Swing", world.location_name_to_id["Swing"], farm
    )
    farm.locations.append(swing)

    dog_house = HorispelagoClassicLocation(
        world.player, "Dog House", world.location_name_to_id["Dog House"], farm
    )
    farm.locations.append(dog_house)

    top_of_silo = HorispelagoClassicLocation(
        world.player, "Top of Silo", world.location_name_to_id["Top of Silo"], farm
    )
    farm.locations.append(top_of_silo)

    over_the_tube = HorispelagoClassicLocation(
        world.player, "Over the Tube", world.location_name_to_id["Over the Tube"], farm
    )
    farm.locations.append(over_the_tube)

    southwest_corn = HorispelagoClassicLocation(
        world.player, "Southwest Corn", world.location_name_to_id["Southwest Corn"], farm
    )
    farm.locations.append(southwest_corn)

    tractor_race = HorispelagoClassicLocation(
        world.player, "Tractor Race", world.location_name_to_id["Tractor Race"], farm
    )
    farm.locations.append(tractor_race)

    ufo_corn = HorispelagoClassicLocation(
        world.player, "UFO Corn", world.location_name_to_id["UFO Corn"], farm
    )
    farm.locations.append(ufo_corn)

    silo_corn = HorispelagoClassicLocation(
        world.player, "Silo Corn", world.location_name_to_id["Silo Corn"], farm
    )
    farm.locations.append(silo_corn)

    horse_fan_club_1 = HorispelagoClassicLocation(
        world.player, "Horse Fan Club 1", world.location_name_to_id["Horse Fan Club 1"], farm
    )
    farm.locations.append(horse_fan_club_1)

    horse_fan_club_2 = HorispelagoClassicLocation(
        world.player, "Horse Fan Club 2", world.location_name_to_id["Horse Fan Club 2"], farm
    )
    farm.locations.append(horse_fan_club_2)

    horse_fan_club_3 = HorispelagoClassicLocation(
        world.player, "Horse Fan Club 3", world.location_name_to_id["Horse Fan Club 3"], farm
    )
    farm.locations.append(horse_fan_club_3)

    the_sacrifice = HorispelagoClassicLocation(
        world.player, "The Sacrifice", world.location_name_to_id["The Sacrifice"], farm
    )
    farm.locations.append(the_sacrifice)

    top_of_barn = HorispelagoClassicLocation(
        world.player, "Top of Barn", world.location_name_to_id["Top of Barn"], farm
    )
    farm.locations.append(top_of_barn)

    upper_barn_rafters = HorispelagoClassicLocation(
        world.player, "Upper Barn Rafters", world.location_name_to_id["Upper Barn Rafters"], farm
    )
    farm.locations.append(upper_barn_rafters)

    lower_barn_rafters_1 = HorispelagoClassicLocation(
        world.player, "Lower Barn Rafters 1", world.location_name_to_id["Lower Barn Rafters 1"], farm
    )
    farm.locations.append(lower_barn_rafters_1)

    lower_barn_rafters_2 = HorispelagoClassicLocation(
        world.player, "Lower Barn Rafters 2", world.location_name_to_id["Lower Barn Rafters 2"], farm
    )
    farm.locations.append(lower_barn_rafters_2)

    dentist = HorispelagoClassicLocation(
        world.player, "Dentist", world.location_name_to_id["Dentist"], farm
    )
    farm.locations.append(dentist)

    behind_barn = HorispelagoClassicLocation(
        world.player, "Behind Barn", world.location_name_to_id["Behind Barn"], farm
    )
    farm.locations.append(behind_barn)

    north_corn = HorispelagoClassicLocation(
        world.player, "North Corn", world.location_name_to_id["North Corn"], farm
    )
    farm.locations.append(north_corn)


    # Glue
    golden_apple = HorispelagoClassicLocation(
        world.player, "Golden Apple", world.location_name_to_id["Golden Apple"], glue
    )
    glue.locations.append(golden_apple)
    golden_apple.place_locked_item(world.create_item("Golden Apple"))

# this is basically for logic rules that aren't going to be randomized
# def create_events(world: HorseRidingClassicWorld) -> None:
#     return # fill this out in a few