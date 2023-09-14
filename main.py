import PySimpleGUI as sg
import island_trader_classes as bl
import window_manipulator as wm
import common_strings as st

debug = False
icon = "icon_boat_0.ico"
print(st.WELCOME_STRING, "loading")

world = bl.World()
initial_location = world.ship.current_location.name
canvas_size = (500, 500)
scale = 100
bottom_left = (scale * -1, scale * -1)
top_right = (scale, scale)

island_list = list(world.island_holder.keys())

# define menu items
reset_menu =  ["Reset", [st.CLEAR_SELECTED_ISLAND, st.CLEAR_ALL_ISLANDS]]
save_menu = ["Save", st.SAVE_ENTRIES]

menu_def = [reset_menu , save_menu]
right_click_menu = reset_menu

#### ---  Header  --- ####

header_row = [[sg.Text(st.HEADER_TEXT_DEFAULT, key = st.HEADER_TEXT, expand_x=True , justification='center')]]

#### ---  Bag Column  --- ####

sell_form_layout = []
buy_form_layout = []
remove_form_layout = [[sg.Combo(list(world.item_holder.keys()), key = st.REMOVE_ITEM_KEY ), sg.Button(st.REMOVE, key = st.REMOVE_ITEM_BUTTON_KEY, expand_x=True)]]

# populate repetive 6(12) rows for sell and buy
buy_sell_row_count = 6  # future features: customize this number
for buyvssell, layout in ((st.BUY_ITEM, buy_form_layout), (st.SELL_ITEM, sell_form_layout)):
    [layout.append( 
    [sg.Combo(list(world.item_holder.keys()), key = st.SELECTED_ITEM_KEY+buyvssell+str(range_num)), 
     sg.Combo(list(bl.Item_Bag.item_modifier_keys.keys()), key = st.SELECTED_ITEM_MOD_KEY+buyvssell+str(range_num)), 
     sg.Text(st.BLANK, key = st.DISPLAY_ITEM_VALUE+buyvssell+str(range_num)) ]) 
     for range_num in range(buy_sell_row_count)]

buy_form_frame =  sg.Frame(title=st.BUYING_HEADER , layout = buy_form_layout, key = st.BUY_ITEM+st.FRAME_KEY, expand_x = True, visible=False)
sell_form_frame = sg.Frame(title=st.SELLING_HEADER , layout = sell_form_layout, key = st.SELL_ITEM+st.FRAME_KEY, expand_x = True, visible=False)
remove_form_frame = sg.Frame(title=st.REMOVE_HEADER, layout = remove_form_layout, key = st.REMOVE+st.FRAME_KEY, expand_x=True, visible=False)

set_bag_values_column = [ 
    [sg.Combo([st.SELECT_ISLAND_NAME_PRMOPT] + island_list, key = st.SELECT_ISLAND_NAME_KEY, default_value=st.SELECT_ISLAND_NAME_PRMOPT), sg.Button(st.SELECT, key = st.ISLAND_SELECTED_BUTTON_KEY)], 
    [sg.Text(st.SELECTED_HEADER_PREFIX),
     sg.Text(st.BLANK, key = st.SELECTED_ISLAND_NAME_DISPLAY_KEY)
    ], 
    [buy_form_frame],
    [   sg.Button(st.AUTO_POPULATE_BUY_BUTTON_TEXT, key = st.AUTO_POPULATE_BUY_KEY, expand_x=True),
        sg.Button(st.AUTO_POPULATE_SELL_BUTTON_TEXT, key = st.AUTO_POPULATE_SELL_KEY, expand_x=True),    ],
    [sell_form_frame] ,
    [remove_form_frame],
    [   sg.Button(st.UPDATE, key = st.UPDATE_BAG_BUTTON_KEY, expand_x=True), 
        sg.Button(st.CLEAR, key = st.CLEAR_BAG_BUTTON_KEY, expand_x=True)    ] 
    ]

#### ---  Map  Column  --- ####
# generate graphs and maps

best_1_out_graph = sg.Graph(
    canvas_size = (canvas_size), graph_bottom_left = bottom_left, graph_top_right = top_right,
    background_color = st.WATER, 
#    enable_events=True, 
#    drag_submits=True, 
    key=st.BEST_1_OUT_GRAPH_KEY)

best_1_out_trade_table = sg.Table(values=world.best_outbound_trades.values.tolist(), headings=list(world.best_outbound_trades),
    auto_size_columns=True, display_row_numbers=False, justification=st.CENTER, key= st.BEST_1_OUT_TABLE_KEY,
    enable_events=True, expand_x=True, expand_y=True, enable_click_events=True)

best_1_out_island_tab = [
    #[sg.Text(st.TAB_1_TITLE, justification=st.CENTER, )], 
    [best_1_out_graph], 
    [best_1_out_trade_table]
]

best_long_path_graph = sg.Graph(
    canvas_size = (canvas_size), graph_bottom_left = bottom_left, graph_top_right = top_right,
    background_color = st.WATER, 
    key=st.BEST_LONG_PATH_GRAPH_KEY)

best_long_path_trade_table = sg.Table(values=world.best_long_path_dummy.values.tolist(), headings=list(world.best_long_path_dummy),
    auto_size_columns=True, display_row_numbers=True, justification=st.CENTER, key= st.BEST_LONG_PATH_TABLE_KEY, num_rows = 8,
    enable_events=True, expand_x=True, expand_y=True, enable_click_events=True)

best_long_path_island_tab = [
    #[sg.Text(st.TAB_2_TITLE, justification=st.CENTER, )], 
    [best_long_path_graph], 
    [best_long_path_trade_table],
    [sg.Text(st.TIME_WARNING)], 
    [sg.B(st.BEST_LONG_PATH_BUTTON_TEXT, key = st.BEST_LONG_PATH_BUTTON_KEY)]
]


#### ---  Ship Column  --- ####

ship_column_capacity = [
    [ # first "row"
            sg.Text(f"{st.CAPACITY}: ", expand_x=True, justification=st.CENTER ), 
           # ],
           # [ # second "row"
            sg.Input(default_text = world.ship.capacity, enable_events=True, key = st.SHIP_CAPASITY_INPUT, size=(10,1) , expand_x=True , justification=st.CENTER)
            ]
            ]
ship_column_bargaining = [
            [ # first "row"
                sg.Text(f"{st.BARGAINING_POWER}:", expand_x=True, justification=st.CENTER ), 
            #],
           # [ # second "row"
                sg.Input(f"{world.ship.bargaining_power_pct}%", enable_events=True, key = st.SHIP_BARGAINING_INPUT , size=(5,1), expand_x=True , justification=st.CENTER), 
            ]
            ]

ship_column_travlepoints= [ # discontinued 
            [ # first "row"
            sg.Text(f"{st.TRAVEL_POINTS}:", expand_x=True , justification=st.CENTER)
            ],
            [ # second "row"
                sg.Input(world.ship.travel_points, enable_events=True, key = st.TRAVEL_POINTS_INPUT, size=(5,1), expand_x=True , justification=st.CENTER), 
            ]
            ]

ship_frame_layout = [# base containiner
    [ # column row
        sg.Column(layout=ship_column_capacity, expand_x=True),
    ], # end column row
    [
        sg.Column(layout=ship_column_bargaining, expand_x=True),
        # sg.Column(layout=ship_column_travlepoints, expand_x=True)
    ], # end column row
    [ # update button - sends for all three to update
        sg.Button(st.UPDATE_SHIP, key= st.UPDATE_SHIP_KEY ,expand_x=False)
    ] ,                 
                     ] # end base container 



mode_row = [sg.T(st.MODE_HEADER)] + [sg.Radio(mode_, group_id=st.WORLD_MODE, key = st.WORLD_MODE_KEY+ mode_, enable_events = True, default = mode_ == world.mode) for mode_ in world.POSIBLE_MODES]

ship_column = [
    [ship_frame],
    [sg.Text(st.LOCATION.format(initial_location), key = st.LOCATION_KEY )], #, sg.Text(initial_location , key = st.LOCATION_KEY )  ],    
    [sg.Combo([st.TRAVEL_ISLAND_NAME_PRMOPT] + island_list, key = st.TRAVEL_ISLAND_NAME_KEY, default_value=st.TRAVEL_ISLAND_NAME_PRMOPT), sg.Button(st.TRAVEL, key = st.TRAVEL_ISLAND_BUTTON_KEY)], 
    # mode_row, # mode row
    [sg.T(st.MODE_HEADER)],
    [sg.Radio(mode_, group_id=st.WORLD_MODE, key = st.WORLD_MODE_KEY+ mode_, enable_events = True, default = mode_ == world.mode) for mode_ in world.POSIBLE_MODES]
]


#### ---  Connection Table  --- ####

connection_table = [  
    
    [sg.Table(
        values=[values[1:] for values in world.trade_from_single_island().values.tolist()],
        headings=list(world.trade_from_single_island())[1:],
        enable_events=True,
        auto_size_columns=True, display_row_numbers=False, justification=st.CENTER, 
        key= st.SHIP_TRADE_TABLE_KEY,
        expand_x=True, expand_y=True, enable_click_events=True)
    ]
    
]
connection_frame = sg.Frame(st.CONNECTIONS.format(initial_location),       
    [[sg.Table(
        values=[values[1:] for values in world.trade_from_single_island().values.tolist()],
        headings=list(world.trade_from_single_island())[1:],
        enable_events=True,
        auto_size_columns=True, display_row_numbers=False, justification=st.CENTER, 
        key= st.SHIP_TRADE_TABLE_KEY,
        expand_x=True, expand_y=True, enable_click_events=True)
    ]],
    key = st.CONNECTIONS_TABLE_TITLE_KEY
    )


#### ---  Footer Row  --- ####

footer_row = [[sg.Text(f'{st.FOOTER_TEXT_PREFIX}None', key = st.FOOTER_TEXT, expand_x=True , justification='center')]]

window_layout = [
    [sg.Menu(menu_def),
        [sg.Frame("frame 1", header_row, expand_x=True)], # header / row1 
        # body / row 2
        [sg.Frame(st.MAP_TITLE,   

            [[sg.TabGroup(
                [[sg.Tab(st.TAB_1_TITLE, best_1_out_island_tab),
                sg.Tab(st.TAB_2_TITLE, best_long_path_island_tab)]])]],
        ),
        sg.Frame("Rigth Side", 
            [
                [sg.Frame("Bags", set_bag_values_column, expand_y=True)],
                [sg.Frame("Ship_",ship_column )], 

            
            [ connection_frame ]])
        ],
    footer_row]
]

# window display trigger
window = sg.Window(st.WELCOME_STRING, window_layout, finalize=True, right_click_menu=right_click_menu, icon=icon, resizable=True) 

##### ------ Initialzie screen manipulators ------ #####
hand_of_god = wm.HandOfGod(window, world, best_1_out_graph, best_long_path_graph)

hand_of_god.draw_map(st.BEST_1_OUT_GRAPH_KEY)

while True:
    event, values = window.read() # event will be the key string of whichever element the user interacts with.
        
    if debug: print(f"{event = }")

    # end program if closed
    if event == 'Exit' or event == sg.WIN_CLOSED:
        hand_of_god.save_triggered()
        break
    else:
        hand_of_god.process_event_input(event, values) 

window.close()