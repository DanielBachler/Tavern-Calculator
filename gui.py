import sys
import fileParser
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

        # Dictionary of rule sets
        rulesets = {}        

        # Get files
        if file_parser.exec_():
            filename = file_parser.selectedFiles()

            # Generate file parser object
            parser = fileParser.FileParser()
            rulesets = parser.parseRuleSetFile(filename)
            

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