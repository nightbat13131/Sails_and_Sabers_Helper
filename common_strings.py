WELCOME_STRING = "Bloodline: Heros of Lithas - Sails and Sabers Helper"

## -- Generic Strings -- ##

BLANK = ""
CENTER = 'center'
CLEAR = 'Clear'
LOCATION = 'Currnet Location: {}'
FRAME_KEY = "-Frame Key-"
LEFT = "left"
NO = "No"
NONE = 'None'
REMOVE = "Remove"
SELECT = 'Select'
SHIP = 'Ship'
TRAVEL = 'Travel'
UPDATE = "Update"
YES = "Yes"

## -- Item Menus -- ##

THE_ISLAND = "the island"
HEADER_TEXT = '-HEADER_TEXT-'
HEADER_TEXT_DEFAULT = WELCOME_STRING.center(75, "~")

SELL_ITEM = 's_item'
BUY_ITEM = 'b_item'

CLEAR_BAG_BUTTON_KEY = '-Clear_bags_button_key-'
CLEAR_SELECTED_ISLAND = 'Clear Selected Island'
CLEAR_ALL_ISLANDS = 'Clear ALL Islands'
SAVE = 'Save'
SAVE_AS = 'Save As'
LOAD = "Load"
SAVE_CONFORMATION_POPUP = "-SAVE_CONFORMATION_POPUP-"
SELECTED_ISLAND_NAME_DISPLAY_KEY = '-SELECTED_ISLAND-'
ISLAND_SELECTED_BUTTON_KEY = '-ISLAND SELECTED-'
SELECTED_HEADER_PREFIX = "Setting Bags for:"
SELECT_ISLAND_NAME_PRMOPT = 'Select an Island to edit.'
SELECT_ISLAND_NAME_KEY = '-holder for currently selected island'
SELECTED_ITEM_KEY = '-selected-item-holder-'
SELECTED_ITEM_MOD_KEY = '-selected_item_mod_holder-'

SELECT_ISLAND_DISPLAY_FRAME_KEY = '-Frame to display or hide island bag settings key-'

DISPLAY_ITEM_VALUE = '-displaying_item_value_after_mod applied'
SELLING_HEADER = 'Selling TO {}'
BUYING_HEADER = 'Buying FROM {}'
REMOVE_HEADER = 'Remove item from {}'
REMOVE_ITEM_KEY = "-REMOVE ITEM KEY-"
ITEM_PROMPT = '-chose item-'

SELLING_KEY_NAME_PREFIX = '-Selling-Name-'
BUYING_KEY_NAME_PREFIX = '-Buying-Name-'

AUTO = "Auto"
AUTO_POPULATE_BUY_BUTTON_TEXT = "<\n<\n<\n<"
AUTO_POPULATE_BUY_KEY = '-AUTO_POPULATE_BUY_KEY-'
AUTO_POPULATE_SELL_BUTTON_TEXT = ">\n>\n>\n>"
AUTO_POPULATE_SELL_KEY = '-AUTO_POPULATE_SELL_KEY-'
UPDATE_BAG_BUTTON_KEY = '-Update_bags_button_key-'
REMOVE_ITEM_BUTTON_KEY = "-Remove Item Button key-"

## -- Maps and Maps' Tables -- ##

MAP_TITLE = "Maps"

TAB_1_TITLE = "Each Island's Best Outgoing Trade"
BEST_1_OUT_GRAPH_KEY = f"-{TAB_1_TITLE} Graph Key-"
BEST_1_OUT_TABLE_KEY = f"-{TAB_1_TITLE} Table Key-"
TAB_2_TITLE = "Best Long Path Between All Entered Islands"
BEST_LONG_PATH_GRAPH_KEY = f"-{TAB_2_TITLE} Graph Key-"
BEST_LONG_PATH_TABLE_KEY = f"-{TAB_2_TITLE} Table Key-"
BEST_LONG_PATH_BUTTON_TEXT = "Calculate"
TIME_WARNING = f"""Calculating the "Best Longest Path" takes several minutes during which the program 
will be unresponsive. This tab only updates with the "{BEST_LONG_PATH_BUTTON_TEXT}" button wereas the 
other tab updates with each change. Make sure your Ship location is correct as that's 
the island the path starts from. This calculation does take skipping islands into 
account. Press the "{BEST_LONG_PATH_BUTTON_TEXT}" button when you are ready."""
BEST_LONG_PATH_BUTTON_KEY = f"-{TAB_2_TITLE} {BEST_LONG_PATH_BUTTON_TEXT} Key -"

#### ---- Map Colors ---- ####

WATER = 'dark turquoise' # "deep sky blue" # 'light sea green'
WATER_HIGHLIGHT = 'pale turquoise'
ISLAND_BODY_0 = 'saddle brown'
ISLAND_BODY_1 = 'chocolate4' # 'brown'
ISLAND_NAME_TEXT_COLOR = 'black'
SHIP_HULL_FILL = 'tan3'
SHIP_HULL_LINE = 'sienna4'
SHIP_SAIL_FILL = 'ivory2' # 'white'
SHIP_SAIL_LINE = 'ivory3' 

## -- Ship and Ship's Table -- ##

TRAVEL_ISLAND_NAME_PRMOPT = 'Select an Island to Travel to'
TRAVEL_ISLAND_NAME_KEY = '-holder for current location island'
TRAVEL_ISLAND_BUTTON_KEY ='-Destination Selected-'
CONNECTIONS = " All Paths Out Of {} "
CONNECTIONS_TABLE_TITLE_KEY = "-connections table title key-"
LOCATION_KEY = '-current location display key-'

SHIP_TRADE_TABLE_KEY = "-Ship Trade Table Key-"

CAPACITY = 'Capacity'
SHIP_CAPASITY_INPUT = '-SHIP_CAPASITY_INPUT-'
BARGAINING_POWER = 'Bargaining Power'
SHIP_BARGAINING_INPUT = '-SHIP_BARGAINING_INPUT-'
UPDATE_SHIP = "Update Ship"
UPDATE_SHIP_KEY = '-UPDATE_SHIP_KEY-'

MODE_HEADER = "Select Focus Mode For Calculations:"
WORLD_MODE = "world_mode"
WORLD_MODE_KEY = "-World mode key:-"

## -- Footer -- ##

FOOTER_TEXT = '-Footer_text-'
FOOTER_TEXT_PREFIX = 'Last command: '

## -- world object strings -- ##

SHIP_PRIMARY_KEY = "ship"
SHIP_LOCACTION_KEY = "current_location"
SHIP_CAPACITY_KEY = "capacity"
SHIP_BARGAINING_KEY = "bargaining_power"
SHIP_SAIL_KEY = "ship_sail"
SHIP_HULL_KEY = 'ship_hull'

ISLAND_PRIMARY_KEY = "nodes"
ISLAND_SELLING_KEY = "selling"
ISLAND_BUYING_KEY = "buying"
ISLAND_LOCATION_KEY = "loc_x_y"
ISLAND_SHAPE_KEY = "shape"
ISLAND_DOCK_KEY = "dock_x_y"
ISLAND_EDGES_KEY = "edges"
ISLAND_UNDIRECTED_KEY = "undirected edges"

ITEM_PRIMARY_KEY = "items"


ISLAND_DATA = {SHIP_PRIMARY_KEY: {SHIP_LOCACTION_KEY: "Samalkan", SHIP_CAPACITY_KEY: 90, SHIP_BARGAINING_KEY: 0, SHIP_SAIL_KEY: [[[-2, 13], [-6, 3], [6, 3], [0, 13]]], SHIP_HULL_KEY: [[[-6, 2], [-4, -2], [4, -2], [6, 2], [0, 2], [0, 12], [-2, 12], [-2, 2]]]}, ITEM_PRIMARY_KEY: [{"name": "Darkhide", "base_value": 70, "weight": 3}, {"name": "Dragonglass", "base_value": 30, "weight": 2}, {"name": "Fresh Fruit", "base_value": 70, "weight": 3}, {"name": "Gold", "base_value": 500, "weight": 10}, {"name": "Gunpowder", "base_value": 150, "weight": 5}, {"name": "Lodestone", "base_value": 150, "weight": 5}, {"name": "Silver", "base_value": 150, "weight": 5}, {"name": "Spices", "base_value": 150, "weight": 5}, {"name": "Spidersilk", "base_value": 70, "weight": 3}, {"name": "Tea Leaf", "base_value": 30, "weight": 2}, {"name": "Titanbone", "base_value": 500, "weight": 10}, {"name": "Witchsteel", "base_value": 70, "weight": 3}], ISLAND_PRIMARY_KEY: {"Abidos": {ISLAND_LOCATION_KEY: [-75, 10], ISLAND_DOCK_KEY: [17, -17], ISLAND_SHAPE_KEY: [[[19, -10], [21, -9], [21, -8], [23, -7], [22, -6], [21, -6], [20, -5], [21, -5], [21, -4], [22, -4], [23, -3], [22, -2], [23, -2], [23, 1], [22, 1], [21, 2], [22, 3], [22, 4], [21, 5], [22, 6], [24, 4], [25, 5], [24, 6], [26, 6], [27, 5], [26, 6], [24, 7], [23, 7], [22, 8], [23, 8], [22, 9], [23, 10], [22, 11], [24, 11], [23, 12], [22, 12], [22, 13], [23, 13], [24, 13], [23, 13], [20, 15], [18, 14], [17, 15], [16, 14], [15, 16], [14, 15], [13, 15], [12, 14], [11, 14], [9, 15], [8, 16], [7, 17], [6, 19], [4, 17], [3, 19], [1, 15], [0, 15], [-1, 16], [-2, 14], [-3, 14], [-2, 13], [-3, 13], [-4, 14], [-5, 14], [-6, 13], [-8, 15], [-10, 14], [-11, 15], [-12, 16], [-12, 15], [-13, 16], [-14, 15], [-16, 14], [-14, 13], [-10, 11], [-8, 12], [-5, 12], [-5, 11], [-4, 10], [0, 9], [1, 8], [1, 6], [-1, 7], [-2, 8], [-3, 7], [-4, 6], [-5, 7], [-6, 6], [-7, 7], [-8, 6], [-10, 8], [-11, 7], [-12, 8], [-13, 8], [-14, 7], [-16, 8], [-14, 9], [-16, 9], [-17, 10], [-18, 9], [-20, 9], [-19, 8], [-20, 7], [-22, 6], [-21, 5], [-18, 5], [-17, 4], [-18, 4], [-17, 3], [-15, 3], [-14, 2], [-14, 1], [-13, 0], [-14, 0], [-14, -1], [-15, -2], [-13, -2], [-13, -3], [-14, -3], [-15, -4], [-16, -3], [-18, -3], [-20, -4], [-22, -4], [-22, -6], [-20, -6], [-19, -7], [-17, -7], [-16, -8], [-15, -8], [-13, -7], [-11, -7], [-11, -6], [-11, -5], [-9, -4], [-11, -3], [-11, -2], [-10, -3], [-9, -3], [-6, -4], [-7, -4], [-6, -4], [-2, -6], [-2, -8], [-3, -9], [-5, -9], [-6, -10], [-5, -11], [-4, -11], [-3, -12], [-4, -12], [-4, -13], [-1, -13], [0, -14], [1, -13], [3, -13], [4, -12], [5, -12], [6, -13], [7, -12], [8, -13], [9, -12], [10, -13], [10, -12], [11, -12], [11, -13], [12, -13], [12, -14], [13, -15], [14, -14], [15, -14], [15, -13], [15, -11], [16, -10], [16, -9]], [[-20, 15], [-21, 15], [-22, 16], [-20, 16]], [[0, -17], [3, -17], [1, -16], [-1, -16]]]}, "Coranzon": {ISLAND_LOCATION_KEY: [-25, 75], ISLAND_DOCK_KEY: [18, -15], ISLAND_SHAPE_KEY: [[[-8, -3], [-8, -5], [-9, -6], [-9, -7], [-10, -7], [-11, -8], [-12, -8], [-12, -9], [-10, -9], [-10, -8], [-8, -8], [-6, -9], [-5, -9], [-6, -10], [-4, -9], [-2, -9], [-2, -11], [-1, -11], [0, -10], [1, -11], [3, -11], [2, -9], [1, -9], [1, -8], [3, -8], [3, -7], [4, -7], [4, -6], [5, -6], [6, -5], [9, -4], [9, -7], [8, -6], [7, -6], [7, -7], [8, -8], [7, -10], [6, -10], [10, -10], [12, -9], [13, -10], [16, -10], [18, -9], [19, -11], [21, -11], [22, -10], [22, -8], [26, -8], [28, -6], [26, -4], [28, -2], [26, -2], [25, 0], [23, -1], [22, 0], [22, 2], [20, 3], [19, 2], [18, 3], [17, 3], [17, 4], [18, 4], [17, 5], [15, 5], [14, 6], [13, 4], [12, 5], [9, 5], [4, 6], [5, 5], [2, 6], [3, 5], [2, 5], [3, 4], [3, 3], [4, 3], [3, 3], [3, 4], [2, 5], [3, 5], [2, 6], [5, 5], [4, 6], [9, 5], [9, 6], [7, 8], [7, 9], [6, 10], [9, 11], [10, 11], [11, 12], [14, 12], [12, 14], [11, 13], [9, 15], [8, 14], [7, 14], [6, 15], [5, 14], [4, 14], [2, 13], [1, 12], [0, 13], [-1, 11], [-1, 8], [-2, 9], [-2, 10], [-3, 10], [-4, 11], [-3, 11], [-6, 12], [-2, 14], [0, 14], [-4, 14], [-5, 15], [-7, 14], [-8, 15], [-9, 14], [-11, 13], [-11, 12], [-12, 12], [-11, 11], [-13, 9], [-12, 8], [-11, 8], [-11, 7], [-12, 7], [-13, 6], [-15, 7], [-15, 6], [-16, 7], [-16, 6], [-18, 5], [-18, 6], [-19, 5], [-22, 5], [-23, 4], [-22, 3], [-23, 3], [-23, 1], [-21, 1], [-21, 0], [-20, -1], [-21, -2], [-22, -1], [-24, -1], [-22, -3], [-21, -3], [-21, -4], [-20, -5], [-19, -4], [-20, -3], [-19, -2], [-16, -2], [-17, -1], [-17, 0], [-16, 0], [-15, 1], [-13, 2], [-9, 1], [-9, 0], [-8, -1], [-6, -1], [-5, 0], [-4, 0], [-4, 1], [-3, 1], [-3, 2], [-2, 2], [-1, 3], [-2, 2], [-3, 2], [-3, 1], [-4, 1], [-4, 0], [-5, 0], [-6, -1], [-7, -2], [-7, -3]]]}, "Hagenport": {ISLAND_LOCATION_KEY: [65, 75], ISLAND_DOCK_KEY: [-13, -11], ISLAND_SHAPE_KEY: [[[22, -15], [21, -17], [20, -17], [21, -19], [20, -21], [19, -24], [18, -24], [18, -27], [12, -30], [14, -29], [16, -29], [16, -28], [18, -27], [19, -27], [20, -26], [20, -25], [22, -24], [24, -22], [25, -18], [25, -14], [24, -13], [23, -9], [22, -8], [21, -6], [22, -5], [24, -5], [24, -4], [22, -3], [23, -2], [22, -1], [21, 1], [19, 1], [18, 3], [17, 4], [17, 5], [16, 5], [16, 6], [15, 7], [12, 7], [11, 6], [8, 6], [7, 5], [6, 6], [5, 6], [5, 5], [6, 4], [4, 2], [5, 0], [5, -1], [7, -2], [10, -3], [11, -5], [13, -6], [13, -7], [14, -8], [12, -10], [13, -12], [15, -11], [16, -11], [17, -12], [20, -13], [20, -14], [21, -14], [22, -15]], [[3, -1], [2, 1], [1, 1], [1, 2], [3, 4], [3, 6], [4, 7], [6, 7], [5, 8], [6, 9], [4, 10], [2, 10], [1, 12], [0, 13], [-1, 13], [-2, 12], [-3, 13], [-4, 12], [-5, 13], [-6, 15], [-7, 14], [-8, 15], [-9, 13], [-10, 14], [-11, 13], [-13, 13], [-13, 12], [-14, 11], [-13, 11], [-14, 10], [-13, 9], [-14, 8], [-13, 7], [-14, 6], [-15, 7], [-17, 6], [-18, 5], [-20, 6], [-21, 6], [-22, 5], [-25, 5], [-29, 4], [-25, 5], [-18, 4], [-15, 4], [-12, 3], [-12, 2], [-10, 2], [-11, 1], [-10, 1], [-10, 0], [-11, -2], [-12, -2], [-11, -3], [-9, -4], [-7, -5], [-7, -6], [-5, -5], [-4, -6], [-2, -5], [-1, -6], [1, -6], [3, -7], [4, -7], [7, -8], [9, -9], [10, -8], [10, -7], [9, -6], [9, -5], [8, -4], [8, -3], [5, -2], [4, -2]], [[-23, 13], [-26, 13], [-27, 14], [-25, 15], [-22, 15], [-21, 14]], [[7, 10], [8, 11], [10, 11], [9, 12], [7, 12], [6, 13], [3, 13], [5, 12], [5, 11], [6, 10]], [[10, 7], [11, 8], [12, 8], [11, 9], [9, 8]], [[12, 9], [14, 9], [14, 8]], [[-15, 1], [-13, 2], [-14, 3], [-16, 3], [-18, 4], [-19, 3], [-20, 4], [-21, 4], [-22, 3], [-22, 2], [-21, 2], [-20, 1], [-18, 2], [-16, 1]]]}, "Dredgewater": {ISLAND_LOCATION_KEY: [75, -70], ISLAND_DOCK_KEY: [2, -14], ISLAND_SHAPE_KEY: [[[-5, -10], [-4, -11], [-3, -10], [2, -10], [2, -9], [4, -8], [5, -9], [7, -8], [7, -7], [8, -7], [9, -6], [9, -5], [8, -5], [6, -3], [8, -2], [7, -2], [8, 0], [10, 2], [11, 1], [13, 3], [12, 2], [11, 4], [11, 5], [13, 5], [14, 7], [15, 7], [17, 6], [16, 9], [15, 10], [14, 10], [14, 11], [12, 15], [10, 16], [8, 18], [7, 17], [5, 18], [4, 17], [3, 19], [2, 18], [1, 19], [1, 20], [3, 22], [3, 27], [2, 25], [2, 24], [0, 23], [0, 22], [-1, 22], [-1, 23], [-2, 21], [-4, 21], [-4, 22], [-5, 20], [-6, 21], [-7, 20], [-8, 20], [-9, 21], [-9, 20], [-8, 19], [-7, 19], [-6, 18], [-5, 19], [-4, 19], [-2, 18], [-2, 17], [-1, 16], [-3, 15], [-1, 15], [1, 14], [2, 14], [2, 13], [1, 14], [0, 13], [-1, 13], [-2, 12], [-4, 11], [-5, 12], [-7, 10], [-7, 11], [-8, 12], [-9, 12], [-10, 14], [-11, 13], [-12, 14], [-13, 14], [-13, 13], [-14, 12], [-12, 10], [-12, 9], [-13, 9], [-14, 10], [-15, 8], [-14, 7], [-15, 6], [-16, 6], [-17, 5], [-19, 7], [-21, 5], [-22, 6], [-24, 5], [-25, 7], [-27, 5], [-28, 5], [-29, 6], [-30, 5], [-30, 6], [-31, 5], [-32, 5], [-31, 4], [-32, 4], [-31, 3], [-30, 3], [-30, 0], [-28, -1], [-27, -1], [-28, -2], [-27, -2], [-27, -4], [-28, -4], [-30, -5], [-30, -7], [-31, -8], [-33, -8], [-31, -9], [-30, -9], [-30, -10], [-28, -11], [-27, -11], [-25, -10], [-24, -11], [-22, -12], [-21, -12], [-21, -13], [-22, -13], [-20, -15], [-18, -14], [-17, -15], [-17, -14], [-18, -13], [-17, -13], [-17, -12], [-16, -11], [-16, -12], [-15, -12], [-15, -11], [-14, -11], [-15, -11], [-15, -10], [-14, -10], [-15, -9], [-14, -8], [-11, -8], [-10, -9], [-9, -8], [-8, -9], [-8, -10], [-9, -11], [-9, -12], [-6, -12]], [[-11, 15], [-10, 17], [-8, 17]], [[10, 21], [9, 19]], [[20, 0], [19, 0], [19, 1], [20, 1], [20, 0], [19, -2], [18, -3], [20, -3], [21, -4], [20, -3], [21, -2], [20, -1], [21, -1]], [[-39, 6], [-38, 7], [-39, 8]], [[-35, 8], [-34, 7], [-36, 7]], [[-25, -13], [-24, -14], [-26, -14]], [[-25, -15], [-24, -16], [-23, -16], [-26, -17]], [[-27, -16], [-28, -15], [-29, -15], [-29, -16], [-30, -17]], [[-29, -18], [-29, -19], [-30, -20], [-31, -19]]]}, "New Morrag": {ISLAND_LOCATION_KEY: [-25, -75], ISLAND_DOCK_KEY: [16, -13], ISLAND_SHAPE_KEY: [[[0, -10], [-3, -9], [-5, -9], [-6, -8], [-8, -7], [-10, -7], [-12, -6], [-13, -7], [-15, -5], [-16, -6], [-16, -4], [-18, -3], [-21, -2], [-23, -3], [-25, -3], [-25, -2], [-26, -1], [-26, 0], [-28, 1], [-29, 2], [-30, 2], [-31, 3], [-33, 3], [-34, 4], [-34, 5], [-36, 7], [-33, 5], [-31, 4], [-28, 4], [-27, 3], [-24, 3], [-23, 4], [-22, 2], [-20, 3], [-18, 2], [-16, 0], [-14, -1], [-13, 0], [-11, 0], [-12, 1], [-14, 1], [-16, 2], [-16, 4], [-17, 4], [-18, 5], [-17, 4], [-18, 6], [-17, 6], [-18, 7], [-21, 7], [-20, 8], [-21, 9], [-20, 8], [-20, 9], [-19, 10], [-18, 9], [-16, 8], [-13, 8], [-11, 9], [-11, 10], [-12, 11], [-14, 12], [-10, 12], [-11, 14], [-9, 14], [-9, 13], [-8, 12], [-6, 11], [-6, 12], [-4, 12], [-3, 11], [-3, 12], [-2, 12], [-2, 13], [-1, 13], [-1, 14], [-3, 16], [-5, 17], [-5, 18], [-3, 18], [-2, 17], [-1, 17], [1, 16], [2, 16], [3, 15], [5, 15], [5, 13], [4, 13], [4, 12], [5, 12], [7, 11], [9, 9], [10, 7], [10, 4], [11, 3], [10, 2], [11, 1], [12, 2], [13, 4], [12, 5], [13, 7], [12, 9], [13, 9], [16, 8], [18, 9], [20, 7], [21, 7], [22, 6], [23, 4], [22, 4], [22, 2], [21, 1], [21, 0], [22, -1], [20, -2], [19, -3], [19, -2], [18, -3], [17, -3], [16, -5], [12, -8], [10, -7], [10, -8], [12, -9], [11, -10], [9, -11], [2, -11]], [[-6, 19], [-9, 19], [-8, 20], [-7, 18]], [[21, 9], [22, 8], [26, 7], [28, 5], [28, 6], [26, 6], [24, 8]], [[23, 3], [23, 2], [24, 0], [26, 2], [27, 2], [26, 1], [24, 1], [24, 2]], [[-25, -12], [-26, -11], [-24, -11]]]}, "Samalkan": {ISLAND_LOCATION_KEY: [20, 0], ISLAND_DOCK_KEY: [1, -16], ISLAND_SHAPE_KEY: [[[5, 0], [5, 1], [7, 3], [9, 3], [11, 4], [14, 5], [15, 5], [17, 4], [17, 2], [22, 3], [23, 2], [25, 2], [26, 1], [27, 2], [27, 3], [28, 4], [25, 4], [26, 5], [25, 7], [26, 7], [27, 6], [28, 6], [28, 7], [26, 7], [25, 8], [26, 8], [24, 9], [23, 9], [23, 10], [21, 11], [18, 12], [20, 12], [19, 13], [18, 12], [16, 13], [16, 14], [15, 14], [12, 13], [11, 12], [11, 11], [9, 11], [9, 10], [7, 10], [7, 9], [6, 8], [5, 10], [4, 10], [3, 11], [0, 11], [-4, 13], [-5, 12], [-6, 15], [-7, 13], [-9, 15], [-10, 14], [-11, 15], [-11, 13], [-12, 12], [-14, 11], [-11, 11], [-12, 9], [-13, 8], [-14, 8], [-15, 7], [-15, 6], [-16, 5], [-15, 5], [-16, 3], [-18, 3], [-20, 2], [-18, 2], [-18, 1], [-16, 2], [-15, 1], [-12, 1], [-13, 0], [-12, -1], [-13, -2], [-14, -2], [-15, -3], [-16, -3], [-18, -5], [-18, -6], [-17, -6], [-18, -8], [-19, -9], [-18, -10], [-17, -10], [-17, -12], [-16, -12], [-17, -13], [-18, -13], [-19, -14], [-21, -15], [-18, -16], [-16, -16], [-16, -17], [-15, -17], [-15, -18], [-12, -18], [-11, -17], [-9, -16], [-7, -16], [-5, -15], [-7, -14], [-7, -11], [-8, -11], [-8, -9], [-6, -8], [-5, -10], [-1, -10], [2, -8], [2, -7], [1, -6], [3, -6], [4, -7], [3, -8], [4, -9], [7, -9], [8, -8], [7, -7], [9, -8], [10, -8], [11, -7], [10, -6], [10, -7], [9, -8], [7, -7], [7, -6], [6, -5], [7, -4], [9, -4], [10, -5], [11, -5], [10, -4], [11, -3], [14, -3], [13, -2], [14, -2], [13, -1], [15, 0], [14, 0], [13, -1], [11, 0], [10, 1], [10, -2], [9, -2], [7, 0]], [[15, -6], [15, -7], [16, -8], [18, -8], [19, -9], [20, -9], [20, -8], [22, -7], [24, -7], [26, -5], [26, -4], [29, -4], [29, -3], [28, -2], [27, -2], [25, -1], [24, 0], [22, -2], [20, -1], [20, -2], [18, -3], [17, -2], [17, -4], [18, -5], [17, -6], [17, -6]], [[-3, 15], [-6, 16], [-4, 14], [-3, 14]], [[-6, 16], [-5, 17], [-2, 16]], [[-22, -1], [-23, -2], [-24, -2]], [[-26, 0], [-23, 2]], [[-24, 3], [-23, 4], [-20, 4], [-21, 5], [-20, 6], [-18, 6], [-20, 7], [-21, 8], [-21, 6], [-22, 6], [-23, 7], [-23, 6], [-25, 5], [-24, 4], [-24, 3], [-26, 2], [-26, 3], [-28, 3], [-29, 4], [-30, 4], [-31, 3], [-31, 2], [-32, 1], [-30, 2], [-29, 2], [-28, 1], [-27, 1]], [[14, 20], [11, 20], [10, 19], [9, 19], [9, 20], [11, 19]], [[-22, -13], [-24, -13], [-25, -12], [-28, -12], [-29, -11], [-29, -13], [-30, -13], [-28, -13], [-29, -14], [-28, -15], [-27, -14], [-24, -14]]]}}, ISLAND_EDGES_KEY: {ISLAND_UNDIRECTED_KEY: [{"nodes": ["Abidos", "Coranzon"], "weight": 1}, {"nodes": ["Abidos", "Hagenport"], "weight": 2}, {"nodes": ["Abidos", "Dredgewater"], "weight": 2}, {"nodes": ["Abidos", "New Morrag"], "weight": 1}, {"nodes": ["Abidos", "Samalkan"], "weight": 1}, {"nodes": ["Coranzon", "Hagenport"], "weight": 1}, {"nodes": ["Coranzon", "Dredgewater"], "weight": 2}, {"nodes": ["Coranzon", "New Morrag"], "weight": 2}, {"nodes": ["Coranzon", "Samalkan"], "weight": 1}, {"nodes": ["Hagenport", "Dredgewater"], "weight": 1}, {"nodes": ["Hagenport", "New Morrag"], "weight": 2}, {"nodes": ["Hagenport", "Samalkan"], "weight": 1}, {"nodes": ["Dredgewater", "New Morrag"], "weight": 1}, {"nodes": ["Dredgewater", "Samalkan"], "weight": 1}, {"nodes": ["New Morrag", "Samalkan"], "weight": 1}]}}

default_save_format = {SHIP_PRIMARY_KEY: {SHIP_LOCACTION_KEY: "Samalkan", SHIP_CAPACITY_KEY: 90, SHIP_BARGAINING_KEY: 0},
  ISLAND_PRIMARY_KEY: 
  {"Abidos": {ISLAND_SELLING_KEY: {}, ISLAND_BUYING_KEY: {}}, 
    "Coranzon": {ISLAND_SELLING_KEY: {}, ISLAND_BUYING_KEY: {}}, 
    "Hagenport": {ISLAND_SELLING_KEY: {}, ISLAND_BUYING_KEY: {}}, 
    "Dredgewater": {ISLAND_SELLING_KEY: {}, ISLAND_BUYING_KEY: {}}, 
    "New Morrag": {ISLAND_SELLING_KEY: {}, ISLAND_BUYING_KEY: {}}, 
    "Samalkan": {ISLAND_SELLING_KEY: {}, ISLAND_BUYING_KEY: {}}}}