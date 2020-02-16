# Dan Bachler
# tavernCalc.py
# A simple application for calculating tavern profits in Dungeons and Dragons Editions 3.5 and 5

from PyQt5.QtCore import QCoreApplication
import gui
import sys

app = None

# Main that inits the window
def main():
    ex = gui.MainUI()
    ex.initUI()

    sys.exit(app.exec_())

# Runs main and sets up environment for GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main()
else:
    print("Unable to execute")