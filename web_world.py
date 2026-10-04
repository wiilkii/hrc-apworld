from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class HorseRidingClassicWebWorld(WebWorld):

    game = "Horse Riding Classic"

    theme = "grassFlowers"

    setup_en = Tutorial(
        "Horse Riding Classic Setup Guide",
        "Setup instructions coming soon.",
        "English",
        "setup_en.md",
        "setup/en",
        [],
    )

    tutorials = [setup_en]