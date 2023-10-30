# Sails_and_Sabers_Helper
Disclamer: I am not afilated with the creators Bloodline Heroes of Lithas. 

This is an app built with Python to help optimize the Sails and Sabers minigame within the Bloodline Heroes of Lithas mobile game. It was born of a desire to optimize trade routs between the islands. As the values change after a few hours, I wanted an interface to that would make entering the information easy. I also build this to see if I could as my first attempt at making a app.

You only need "Bloodline Heros of Lithas - Sails and Sabers Helper.exe" to run the app as an exicutable. If you are familar with python, or otherwise want to take a look at the coding, you are welcome to look at the other files. 

## This App is broken into two primary sections: Maps and Controls. 

### Maps:
Display a map of the islands along with arrows highliting differnet trades based on the mode selected in the Conrol section. A table bellow the map lists the information shown by the arrows. Tabs let the user swtich between "Best Outgoing trades" and "Best long path." A little ship icon shows on the Current island to indicate the starting position or point of origin for the calculations. 

#### Best Outgoing trades
This map automaticly udpates with every change to the controls.
The island selected as the "Current Island" in the Ship Control is the point of origin for the outgoing trades. This map and the table below show the list each other island and what item would be best bought at the current island to be sold at the destination island. If there is a tie, both will show in the table. 

#### Best long path
This map only updates when you press the Calculate button. The recursive search through the posible paths you could take and the comparison on the said results can take a few minutes to run, thus is only called on demand. If you want an island removed from the calculation, you can clear it's bags in the controls. The rout calculated seven steps. 

### Controls: 
These sections let you edit and view various details about the islands and the ship. 

#### Select an Island to edit
After you select and island from the dropdown, the user is presened with the ability to control the buy and sell list for the island. Each list is refered to as a bag - so each island has it's own Sell Bag and Buy Bag. The 12 items availbe in the Sail and Sabers mini game are selectable from the dropdowns within the bags. Next to the item dropdown is the corrasponding item modifiter. As the ship trait bargaining power effects these modidifiers and can change, the modifiers are express as symboles instead of absolute values. At 0% bargaining power, the modifiers are +30%, +15%, +0%, -15%, and -30% and the symbols respectivly are ++, +, 0 or blank, -, --. After you populate the Bags, press update to comit the information, otherwise you will loose your work when you select a different island.

Between the Buy Bag and Sell Bag is a "Auto" section with buttons that point to either side. The auto button will populate the Bag it is pointing to based on the other bag. This lets the user select the six items being sold at an island, then instead of having to select the other six items being purchased, the auto bag will populate those 6 items for the user. It order of the items is alphabetical. 

The tool does not track how many items are in each port. If a port rund out of items, select that item in the "Remove item from <selected island>" then press the remove button. This will remove the item from the island's bags and thus remove that item from any calculations related to the island. This remove function is also useful if an item is entered inforrectly and you don't want to clear the entier island to fix the one mistake. 

If you need to clear all the islands (like when the island reset and have all new items), you can do so from the top menu > "Reset" > "Clear All Islands". This option is also avaible when you right click. These menus also have "Clear Selected Island" in case you need to correct a mistake, or just want to exclude the island from calculations. The "Clear" button in the island control will only clear the selected island. 

#### Ship
Ship centric information. Here the user can set the Capacity and Bargaining power of thier ship. After editing these values, press "Update Ship" to commit the changes. These values are used in other parts of the application in caculating trade values. As observed in the Sails and Sabers minigame, Bargaining power only effects the purchase cost when buying items from islands, not the sale cost when selling to other islands. Capacity is used along with item weights to caluclate the maximum number of items the ship can carry. 

Ship section also lets the user set the current island location. This location is the basis of the primary calucations for the tool. After selecting an island from the dropdown, use the "Travel" button to commit the change. 

#### All Path Out Of <Current Island>
The focus island for this table is set in the "Ship" section. It displays all outgoing trades from the Island, profitable or not. The table shows how much it costs to purchat the max number of holdable items at the current island. Reminder, the tool does not know how many items are at a location, so your in game max amount may be lower if you have a high capacity. This is also why the table does not only show the "best" path option, so that the user can build thier purhcase lists of any number of factors. The trades or ordered from best to worse based on the mode the tool is in. The default mode is "Revenue/MC" because the game's ranking is only bassed on Revenue. The mode can be chaanged with the radio buttons under the table. 

#### Modes: 
##### Income: 
Incoming gold from selling items - Outgoing gold to from initial items' purchase.
- useful when you need to increase your overall gold.
##### Revenue/MC: 
Incoming gold from selling items / Trade Points cost to move from current island to destination island. 
- Obtain The most gold for the Points Leaderboards per Trade Point. 
##### Revenue: 
Incoming gold from selling items.
- Obtain The most gold for the Points Leaderboards. While I think Revenue/MC is superior, I'm not going to make that desision for you. 

### Misc
#### Save or Save As
You can save your entries from the top menu. You are also prompted to save when you exit the tool. Save As prompts you for a location and name first. If you have not loaded or saved during the current sesion, Save will trigger the Save As prompt. If Save/Save As fails, an error will show in the Conformation text.

#### Load
You can load information you saved via the Save or Save As option. Best long path will need to be recalculated.  If Load fails, an error will show in the Conformation text.

#### Conformation
There is conformation text at the bottom on the screen that will confirm most actions taken with the tool. If an error prevents a save or load, the failed message will show here.  