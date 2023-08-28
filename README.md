# Sails_and_Sabers_Helper
Disclamer: I am not afilated with the creators Bloodline Heroes of Lithas. 

This is an app built with Python to help optimize the Sails and Sabers minigame within the Bloodline Heroes of Lithas mobile game. It was born of a desier to optimize trade routs between the islands. As the values change after a few hours, I wanted an interface to that would make entering the information easy. 

App is broken into three sections: Left, Middle, Right. 
Left:
Users manage the items availabe for purchase and sale at each island. After selecting a island from the dropdown, users can add items to each Sell and Buy catagory along with the motifiers.   The tool does not track how many items are in each port.

Middle:
Display a map of the islands along with arrows highliting differnet trades based on the mode selected in the Right section. A table bellow the map lists the information shown by the arrows. Tabs let the user swtich between "Best Outgoing trades" and "Best long path."

Right:
Ship centric information. Here the user can set the Capacity and Bargaining power of thier ship. These values are used in other parts of the application in caculating trade values. As observed in the Sails and Sabers minigame, Bargaining power only effects the purchase cost when buying items from islands, not the sale cost when selling to other islands. Capacity is used along with item weights to caluclate the maximum number of items the ship can carry. 

