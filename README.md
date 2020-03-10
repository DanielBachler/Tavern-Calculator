# Tavern-Calculator

A simple to use program to do Tavern profit calculations in DND.  Support V3.5 and V5

# Required Libraries

- PyQt5

# Use

Currently to use the program it must be run from command line with all proper libraries installed to your python interpreter.  

Future plans are to have the program frozen to an executable state that does not require having python installed.

Once the program is launched you will have to select you rule set file, using the file menu on the application then load the tavern you wish to do calculations for.  Hit the update button to randomly select an event and recalculate the values for the tavern. 

To save a tavern there is an option in the file menu that allows for saving the tavern to a file.

To make a new tavern simply select the new tavern button from the tavern menu and fill out the appropriate fields then click save.  This will not save the tavern to a file, but rather save it as the currently active tavern in the program.  To save to a file please use the save tavern button in the file menu.

# Rule Set Formats

For an example please look at the `Inn Events.txt` file.  The general format should be:

```Number whatever description is wanted (effects)``` 

With a  `*` for a special even that repeats in the opening parentheses.

EX:

`06 Local Corrupt official black mails inn (*-50% Income This event continues every month till the Corrupt Official is dealt with)`