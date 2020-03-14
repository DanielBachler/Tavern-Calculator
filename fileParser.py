# fileParser.py
# By: Dan Bachler
# Created 3-14-20
# A refactor of the file parsing system, to better utilize component based programming
# By splitting out the file parser for tavern rule sets anyone can rewrite the parser to meet the needs of their file

import object

class FileParser:

    # Keywords for effects
    keywords = [
        "lose all", #0
        "rent", #1
        "tax", #2
        "upkeep", #3
        "stock", #4
        "employee pay", #5
        "income", #6
        "popularity" #7
    ]

    # Keywords for effect application
    basis_keywords = [
        "permanently",
        "month"
    ]

    # Init the FileParser object (Currently doesn't need to do anything)
    def __init__(self):
        pass

    # parseFile: Parses a given filename from a QFileDialog Widget into a dictionary of rule set objects
    # ARGS: filename (List[String] {From QFileDialog})
    # RETURNS: ruleset (Dict{int => object.RuleSet})
    def parseRuleSetFile(self, filename):
        # Init dictionary
        ruleset = {}

        f = open(filename[0], 'r')
        # Set number offset to 2, increase once numbers get to 99
        number_offset = 2
        # Read each line
        for line in f:
            # Replace fake spaces with real spaces
            line = line.replace(u'\xa0', ' ')
            # Lowercase the whole line
            line = line.lower()

            # Get number test
            number = int(line[:line.index(" ")])
            
            # Get effects out of ruleset
            open_paren = line.index("(")
            close_paren = line.index(")")
            values = line[open_paren+1:close_paren]
            # Split rule list into command list
            values = values.split(",")
            # Get RuleSet object
            rules = self.command_parser(values)
            # Store in dictionary 
            ruleset[number] = rules
        
        return ruleset
    
    # command_parser: Takes in a single command line and turns it into a RuleSet object
    # ARGS: cmd_list (List[String])
    # RETURNS: ? (object.RuleSet)
    def command_parser(self, cmd_list):
        ruleset = object.RuleSet()
        print(cmd_list)
        for command in cmd_list:
            
            ## Branching logic for determining effect

            # Check if lose all
            if self.keywords[0] in command:
                pass
            # Check if rent or tax
            elif self.keywords[1] in command or self.keywords[2] in command:
                pass
            # Check if upkeep
            elif self.keywords[3] in command:
                pass
            # Check if stock
            elif self.keywords[4] in command:
                pass
            # Check if employee pay
            elif self.keywords[5] in command:
                pass
            # Check if income
            elif self.keywords[6] in command:
                pass
            # Check if popularity
            elif self.keywords[6] in command:
                pass

            ## Branching logic to determine if single application or repeating

            # Check if permanent
            if self.basis_keywords[0] in command:
                pass
            # Check if monthly repeating
            elif self.basis_keywords[1] in command:
                pass

            # Check if event is a special event
            if "*" in command:
                ruleset.special = True
    
    # getMultiplier: Pulls the percent value out of the command string and returns a multiplier
    # ARGS: command (String)
    # RETURNS: multiplier (float)
    def getMultiplier(self, command):
        pass
