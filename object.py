# Tavern class, will store information about a tavern
class Tavern:

    ## Base values for tavern
    # Income gained per time period for game
    income = 0
    # Stock price per time period
    stock = 0
    # Employee pay ptp
    pay = 0
    # Rent/Upkeep ptp
    rent = 0
    # Upkeep cost ptp
    upkeep = 0
    # Popularity, starts at 0
    popularity = 0
 
    # __init__: Creates the Tavern object
    # ARGS: self (object.Tavern)
    # RETURNS: object.Tavern
    def __init__(self):
        pass


# A class for the rule sets, will determine tavern value with a calculate function
class RuleSet:

    # If rule is a special event
    special = False

    # If a rules effects are permanent
    permanent = False

    # Multipliers for effects (base = 1 for no change)
    income = 1
    rent = 1
    pay = 1
    upkeep = 1
    stock = 1

    # Popularity effect (base = 0 for no change)
    popularity = 0

    # Initializes the RuleSet object, currently does nothing
    def __init__(self):
        pass