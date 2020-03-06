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

        # Central Widget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        
        # Final setup
        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Tavern Calculator')
        self.show()

    # fileParserRules: Takes in a string for a filename that contains a rule set and returns a dictionary of rules
    # ARGS: self (QMainWindow), file (String)
    # RETURNS: ?? (Dict{int:??})
    def fileParserRules(self, file):
        pass

    # fileParserTavern: Takes a string for a filename that contains the information about the tavern
    # ARGS: self (QMainWindow), file (String)
    # RETURNS: ?? (object.Tavern)
    def fileParserTavern(self, file):
        pass