from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import HorseRidingClassicWorld



def set_all_rules(world: HorseRidingClassicWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_rules(world)

def set_all_entrance_rules(world: HorseRidingClassicWorld) -> None:

    forest_to_desert = world.get_entrance("Forest to Desert")
    forest_to_farm = world.get_entrance("Forest to Farm")
    desert_to_city = world.get_entrance("Desert to City")
    farm_to_city = world.get_entrance("Farm to City")
    farm_to_glue = world.get_entrance("Farm to Glue")
    city_to_glue = world.get_entrance("City to Glue")

    can_go_to_desert = Has("DesertKey", world.player)
    can_go_to_farm = Has("FarmKey", world.player)
    can_go_to_city = Has("CityKey", world.player)
    can_go_to_glue = Has("GlueKey", world.player)

    world.set_rule(forest_to_desert, can_go_to_desert)
    world.set_rule(forest_to_farm, can_go_to_farm)
    world.set_rule(desert_to_city, can_go_to_city)
    world.set_rule(farm_to_city, can_go_to_city)
    world.set_rule(farm_to_glue, can_go_to_glue)
    world.set_rule(city_to_glue, can_go_to_glue)

def set_all_location_rules(world: HorseRidingClassicWorld) -> None:
    has_access_to_desert = Has("DesertKey")
    has_access_to_farm = Has("FarmKey")
    has_access_to_city = Has("CityKey")
    has_access_to_glue = Has("GlueKey")

    stuck_between_an_apple_and_a_hard_place = world.get_location("Stuck Between an Apple and a Hard Place")
    world.set_rule(stuck_between_an_apple_and_a_hard_place, has_access_to_desert)

    apple_casino_1 = world.get_location("Apple Casino 1")
    world.set_rule(apple_casino_1, has_access_to_desert)

    apple_casino_2 = world.get_location("Apple Casino 2")
    world.set_rule(apple_casino_2, has_access_to_desert)

    apple_casino_3 = world.get_location("Apple Casino 3")
    world.set_rule(apple_casino_3, has_access_to_desert)

    tumbleweed = world.get_location("Tumbleweed")
    world.set_rule(tumbleweed, has_access_to_desert)

    an_apple_is_an_egg_right_nest = world.get_location("An Apple is an Egg Right? (Nest)")
    world.set_rule(an_apple_is_an_egg_right_nest, has_access_to_desert)

    is_that_a_seagull_bird_apple_bitch_ass_bird_b_a_b = world.get_location("Is that a seagull? (Bird Apple) (Bitch Ass Bird = B.A.B.)")
    world.set_rule(is_that_a_seagull_bird_apple_bitch_ass_bird_b_a_b, has_access_to_desert)

    arch_apple_i_use_arch_btw = world.get_location("Arch Apple (i use arch btw)")
    world.set_rule(arch_apple_i_use_arch_btw, has_access_to_desert)

    on_the_arch_apple = world.get_location("On the Arch Apple")
    world.set_rule(on_the_arch_apple, has_access_to_desert)

    old_old_town_entrance = world.get_location("Old Old Town Entrance")
    world.set_rule(old_old_town_entrance, has_access_to_desert)

    shoot_horseboy = world.get_location("Shoot Horseboy")
    world.set_rule(shoot_horseboy, has_access_to_desert)

    jail = world.get_location("Jail")
    world.set_rule(jail, has_access_to_desert)

    top_of_saloon = world.get_location("Top of Saloon")
    world.set_rule(top_of_saloon, has_access_to_desert)

    top_of_cactus = world.get_location("Top of Cactus")
    world.set_rule(top_of_cactus, has_access_to_desert)

    fire_ring = world.get_location("Fire Ring")
    world.set_rule(fire_ring, has_access_to_desert)

    cactus_ring = world.get_location("Cactus Ring")
    world.set_rule(cactus_ring, has_access_to_desert)

    wait_i_m_goated_daredevil = world.get_location("Wait I'm Goated (Daredevil)")
    world.set_rule(wait_i_m_goated_daredevil, has_access_to_desert)

    underground_island = world.get_location("Underground Island")
    world.set_rule(underground_island, has_access_to_desert)

    in_between_a_stelagmite_and_a_stelagtite_i_cant_spell = world.get_location("In between a stelagmite and a stelagtite (i cant spell")
    world.set_rule(in_between_a_stelagmite_and_a_stelagtite_i_cant_spell, has_access_to_desert)

    chuck_s_apple = world.get_location("Chuck's Apple")
    world.set_rule(chuck_s_apple, has_access_to_desert)

    canyon_ledge = world.get_location("Canyon Ledge")
    world.set_rule(canyon_ledge, has_access_to_desert)

    between_the_rocks = world.get_location("Between the Rocks")
    world.set_rule(between_the_rocks, has_access_to_desert)

    trench_apple_towards_the_north = world.get_location("Trench Apple (Towards the north)")
    world.set_rule(trench_apple_towards_the_north, has_access_to_desert)

    south_trench = world.get_location("South Trench")
    world.set_rule(south_trench, has_access_to_desert)

    gorge_runner = world.get_location("Gorge Runner")
    world.set_rule(gorge_runner, has_access_to_desert)

    crane = world.get_location("Crane")
    world.set_rule(crane, has_access_to_city)

    crane_cockpit = world.get_location("Crane Cockpit")
    world.set_rule(crane_cockpit, has_access_to_city)

    subway = world.get_location("Subway")
    world.set_rule(subway, has_access_to_city)

    subway_bathroom = world.get_location("Subway Bathroom")
    world.set_rule(subway_bathroom, has_access_to_city)

    west_low_h_building = world.get_location("West Low H Building")
    world.set_rule(west_low_h_building, has_access_to_city)

    east_low_h_building = world.get_location("East Low H Building")
    world.set_rule(east_low_h_building, has_access_to_city)

    west_high_h_building = world.get_location("west High H Building")
    world.set_rule(west_high_h_building, has_access_to_city)

    east_high_h_building = world.get_location("east High H Building")
    world.set_rule(east_high_h_building, has_access_to_city)

    sewer_pipe = world.get_location("Sewer Pipe")
    world.set_rule(sewer_pipe, has_access_to_city)

    city_s_edge_se = world.get_location("City's Edge (SE)")
    world.set_rule(city_s_edge_se, has_access_to_city)

    se_in_between_buildings = world.get_location("SE In Between Buildings")
    world.set_rule(se_in_between_buildings, has_access_to_city)

    that_fucking_bird_that_i_hate = world.get_location("That Fucking Bird That I Hate")
    world.set_rule(that_fucking_bird_that_i_hate, has_access_to_city)

    eat_this_apple_sign = world.get_location("Eat This Apple? Sign")
    world.set_rule(eat_this_apple_sign, has_access_to_city)

    top_of_building_north = world.get_location("Top of Building (North)")
    world.set_rule(top_of_building_north, has_access_to_city)

    ledge_of_building_north = world.get_location("Ledge of Building (North)")
    world.set_rule(ledge_of_building_north, has_access_to_city)

    cardboard_building_north = world.get_location("Cardboard Building North")
    world.set_rule(cardboard_building_north, has_access_to_city)

    cardboard_building_south = world.get_location("Cardboard Building South")
    world.set_rule(cardboard_building_south, has_access_to_city)

    parking_garage_1 = world.get_location("Parking Garage 1")
    world.set_rule(parking_garage_1, has_access_to_city)

    parking_garage_2 = world.get_location("Parking Garage 2")
    world.set_rule(parking_garage_2, has_access_to_city)

    parking_garage_3 = world.get_location("Parking Garage 3")
    world.set_rule(parking_garage_3, has_access_to_city)

    top_of_building_south = world.get_location("Top of Building South")
    world.set_rule(top_of_building_south, has_access_to_city)

    ledge_west = world.get_location("Ledge (West)")
    world.set_rule(ledge_west, has_access_to_city)

    water_overlook_pier_bridge_thingy = world.get_location("Water Overlook Pier Bridge Thingy")
    world.set_rule(water_overlook_pier_bridge_thingy, has_access_to_city)

    doctor_evil = world.get_location("Doctor Evil")
    world.set_rule(doctor_evil, has_access_to_city)

    with_the_tractors = world.get_location("With the Tractors")
    world.set_rule(with_the_tractors, has_access_to_farm)

    in_the_tractor = world.get_location("In the Tractor")
    world.set_rule(in_the_tractor, has_access_to_farm)

    ufo_apple_1 = world.get_location("UFO Apple 1")
    world.set_rule(ufo_apple_1, has_access_to_farm)

    ufo_apple_2 = world.get_location("UFO Apple 2")
    world.set_rule(ufo_apple_2, has_access_to_farm)

    ufo_apple_3 = world.get_location("UFO Apple 3")
    world.set_rule(ufo_apple_3, has_access_to_farm)

    god = world.get_location("God?")
    world.set_rule(god, has_access_to_farm)

    swing = world.get_location("Swing")
    world.set_rule(swing, has_access_to_farm)

    dog_house = world.get_location("Dog House")
    world.set_rule(dog_house, has_access_to_farm)

    top_of_silo = world.get_location("Top of Silo")
    world.set_rule(top_of_silo, has_access_to_farm)

    over_the_tube = world.get_location("Over the Tube")
    world.set_rule(over_the_tube, has_access_to_farm)

    southwest_corn = world.get_location("Southwest Corn")
    world.set_rule(southwest_corn, has_access_to_farm)

    tractor_race = world.get_location("Tractor Race")
    world.set_rule(tractor_race, has_access_to_farm)

    ufo_corn = world.get_location("UFO Corn")
    world.set_rule(ufo_corn, has_access_to_farm)

    silo_corn = world.get_location("Silo Corn")
    world.set_rule(silo_corn, has_access_to_farm)

    horse_fan_club_1 = world.get_location("Horse Fan Club 1")
    world.set_rule(horse_fan_club_1, has_access_to_farm)

    horse_fan_club_2 = world.get_location("Horse Fan Club 2")
    world.set_rule(horse_fan_club_2, has_access_to_farm)

    horse_fan_club_3 = world.get_location("Horse Fan Club 3")
    world.set_rule(horse_fan_club_3, has_access_to_farm)

    the_sacrifice = world.get_location("The Sacrifice")
    world.set_rule(the_sacrifice, has_access_to_farm)

    top_of_barn = world.get_location("Top of Barn")
    world.set_rule(top_of_barn, has_access_to_farm)

    upper_barn_rafters = world.get_location("Upper Barn Rafters")
    world.set_rule(upper_barn_rafters, has_access_to_farm)

    lower_barn_rafters_1 = world.get_location("Lower Barn Rafters 1")
    world.set_rule(lower_barn_rafters_1, has_access_to_farm)

    lower_barn_rafters_2 = world.get_location("Lower Barn Rafters 2")
    world.set_rule(lower_barn_rafters_2, has_access_to_farm)

    dentist = world.get_location("Dentist")
    world.set_rule(dentist, has_access_to_farm)

    behind_barn = world.get_location("Behind Barn")
    world.set_rule(behind_barn, has_access_to_farm)

    north_corn = world.get_location("North Corn")
    world.set_rule(north_corn, has_access_to_farm)

    golden_apple = world.get_location("Golden Apple")
    world.set_rule(golden_apple, has_access_to_glue)


def set_completion_rules(world: HorseRidingClassicWorld) -> None:
    world.set_completion_rule(Has("Golden Apple"))
    

