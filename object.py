# Tavern class, will store information about a tavern
class Tavern:
 
    # __init__: Creates the Tavern object
    # ARGS: self (object.Tavern)
    # RETURNS: object.Tavern
    def __init__(self):
        pass


# A class for the rule sets, will determine tavern value with a calculate function
class RuleSet:

    # If rule is a special event
    special = False

    # Multipliers for effects
    income_effect = 0
    rent = 0
    pay = 0
    upkeep = 0
    stock = 0

    # Popularity effect (additive)
    popularity = 0

    # Initializes the RuleSet object, currently does nothing
    def __init__(self):
        pass