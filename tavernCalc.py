# Dan Bachler
# tavernCalc.py
# A simple application for calculating tavern profits in Dungeons and Dragons Editions 3.5 and 5

from PyQt5.QtWidgets import QApplication
import gui
import sys

app = None

# Main that inits the window
def main():
    app = QApplication(sys.argv)
    ex = gui.MainUI()
    ex.initUI()

    sys.exit(app.exec_())

main()