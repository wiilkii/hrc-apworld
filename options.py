from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle







@dataclass
class HorseRidingClassicOptions(PerGameCommonOptions):
    """
    Options for Horse Riding Classic
    """

    \

    # im not going to worry about options *yet*

    # Example options
    # example_toggle: Toggle = Toggle(False, "Example Toggle", "This is an example toggle option.")
    # example_choice: Choice = Choice(
    #     0,
    #     "Example Choice",
    #     "This is an example choice option.",
    #     [("Option 1", 0), ("Option 2", 1), ("Option 3", 2)],
    # )
    # example_range: Range = Range(
    #     5, "Example Range", "This is an example range option.", (1, 10)
    # )