import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainUI(QMainWindow):

    # __init__: creates the window and initializes variables
    # ARGS: self (QMainWindow)
    # RETURNS: (gui.MainUI (QMainWindow))
    def __init__(self):
        super().__init__()

    # initUI: Creates the UI for the window
    # ARGS: self (QMainWindow)
    # RETURNS: None
    def initUI(self):
        # Menu bar
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")

        # Menu bar actions
        open_tavern = QAction("Open Tavern", self)
        open_tavern.triggered.connect(self.fileParserTavern)

        save_tavern = QAction("Save Tavern", self)
        save_tavern.triggered.connect(self.saveTavernFile)

        load_ruleset = QAction("Load Rule Set", self)
        load_ruleset.triggered.connect(self.fileParserRules)

        # Add actions to menu bar
        file_menu.addAction(open_tavern)
        file_menu.addAction(save_tavern)
        file_menu.addAction(load_ruleset)

        # Central Widget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        
        # Final setup
        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Tavern Calculator')
        self.show()

    # fileParserRules: Takes in a string for a filename that contains a rule set and returns a dictionary of rules
    # ARGS: None
    # RETURNS: ?? (Dict{object.RuleSet:??})
    def fileParserRules(self, file):
        # Make FileDialog object and set parameters
        file_parser = QFileDialog()
        file_parser.setAcceptMode(QFileDialog.AcceptOpen)
        file_parser.setFileMode(QFileDialog.AnyFile)

        # Init filename var
        filename = ""

        # Init dictionary
        ruleset = {}

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

        # Keywords for basis"
        basis_keywords = [
            "permanently",
            "month"
        ]

        # Get files
        if file_parser.exec_():
            filename = file_parser.selectedFiles()
            f = open(filename[0], 'r')
            # Set number offset to 2, increase once numbers get to 99
            number_offset = 2
            # Read each line
            for line in f:
                # Replace fake spaces with real spaces
                line = line.replace(u'\xa0', ' ')
                # Lowercase the whole line
                line = line.lower()
                # Get the number for the event
                number = int(line[0:number_offset])
                # At 99 increase offset
                if number == 99:
                    number_offset += 1 
                
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
                
    # command_parser: Takes in a single command line and turns it into a RuleSet object
    # ARGS: cmd_list (List[String])
    # RETURNS: ? (object.RuleSet)
    def command_parser(self, cmd_list):
        ruleset = object.RuleSet()
        for command in cmd_list:
            pass

    # fileParserTavern: Takes a string for a filename that contains the information about the tavern
    # ARGS: None
    # RETURNS: ?? (object.Tavern)
    def fileParserTavern(self):
        print("Tavern parser")

    # saveTavernFile: Saves the currently loaded tavern into a file
    # ARGS: None
    # RETURNS: ??
    def saveTavernFile(self):
        print("Save tavern")