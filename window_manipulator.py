import math
import common_strings as helper
import PySimpleGUI as sg

debug = False

class Arrow():
    cut_short = 11
    line_thickness = 3
    color = 'gray70'
    text_color = 'black'
    arrow_angle = math.radians(20)
    arrow_leg_length = 10

    def __init__(self, canvas, from_island , to_island , item_name: str, value: int, draw_now: bool = True) -> None:
        self.canvas = canvas
        self.from_island = from_island.loc_x_y
        self.to_island = to_island.loc_x_y
        self.item_name = item_name
        self.value = value
        if draw_now:
            self.draw_arrow()
            # call draw arrow function
            pass

    @property
    def start_point(self):
        output = self.point_from_radian(self.from_island, self.radian_forward, self.cut_short+2)
        return output
    
    @property
    def end_point(self):
        output = self.point_from_radian(self.to_island, self.radian_backward, self.cut_short)
        return output

    @property
    def half_length(self):
        return math.dist(self.to_island, self.from_island)/2

    @property
    def radian_forward(self):
        xs, ys = self.from_island
        xe, ye = self.to_island
        x_delta = xe - xs
        y_delta = ye - ys
        try: # not vertical
            radian = math.atan(y_delta/x_delta)
            if x_delta < 0:  # left vs right
                #print("west/left")
                return radian + math.pi
            else:
                #print("east/right")
                return radian
        except: # veritical line
            if y_delta >= 0: # up vs down
                #print('north/up')
                return math.pi/2 
            else:
                #print("south/down")
                return math.pi/-2

    @property
    def radian_backward(self):
        return self.radian_forward  + math.pi

    @property          
    def midpoint(self) -> tuple:
        xs, ys = self.from_island
        xe, ye = self.to_island
        return ((xe+xs)/2,(ye+ys)/2)

    @property
    def triangle_points(self) -> list: 
        points = [self.end_point]
        for radian in (self.radian_backward + self.arrow_angle, self.radian_backward - self.arrow_angle):
            points.append(self.point_from_radian(self.end_point, radian, self.arrow_leg_length))
        return points

    def point_from_radian(self, origin_point: tuple, radian: float, length) -> tuple:
        """ Find a point "length" away from origin_point in the direction of radian. """
        x_delta = math.cos(radian)*length
        y_delta = math.sin(radian)*length
        x_out = origin_point[0] + x_delta
        y_out = origin_point[1] + y_delta
        return (x_out, y_out)

    def draw_arrow(self) -> None:
        if debug: self.canvas.draw_line(self.from_island, self.to_island, color = 'black', width = 2)
        # drawing line
        self.canvas.draw_line(self.end_point, self.start_point, color = self.color, width = self.line_thickness)
        # draw arrow
        self.canvas.draw_polygon(points = self.triangle_points, fill_color = self.color , line_width = self.line_thickness, line_color = self.color  )
        # draw text
        text0 = f"{self.item_name}\n{self.value}\n\n"
        self.canvas.draw_text(text = text0, location = self.midpoint, angle = math.degrees(self.radian_forward), color = self.text_color, font=None, text_location=helper.CENTER )


class Cartographer():
    island_width = 10
    island_shore = 2

    def __init__(self, world, canvas, canvas_key) -> None:
        self.world = world
        self.canvas = canvas      
        self.bottom_left = canvas.BottomLeft
        self.top_right = canvas.TopRight
        self.canvas_size = canvas.CanvasSize

        
    def draw_map(self, table):
        if debug: print("draw_map")
        self.canvas.draw_rectangle(self.bottom_left, self.top_right, helper.WATER) 
        self.draw_islands()
        self.draw_arrows(table)
        self.draw_ship()

    def draw_arrows(self, table):
        for each in table: # self.world.best_outbound_trades.values.tolist():
            item_name = each[2]
            profit = each[3]
            if profit == None or item_name == self.world.NO_MATCH:
                return
            else:
                from_name = each[0]
                to_name = each[1]
                holder = self.world.island_holder
                from_island_py = holder[from_name]
                to_island_py = holder[to_name]

                Arrow(self.canvas, from_island_py, to_island_py, item_name, profit)

    def draw_islands(self) -> None:
        if debug: print("draw_islands")
        
        for island_name, island_py in self.world.island_holder.items():
            x, y = island_py.loc_x_y
            if debug: print(f"drawing {island_name} {(x, y)=} ")
            if island_py.shapes is not None:
                for each_shape in island_py.shapes:
                    self.canvas.draw_polygon(
                        points = each_shape, fill_color=helper.ISLAND_BODY_1,
                        line_color=helper.WATER_HIGHLIGHT, line_width = self.island_shore
                    )
            else:
                self.canvas.draw_circle((x, y), self.island_width, fill_color=helper.ISLAND_BODY_1, line_color=helper.WATER_HIGHLIGHT, line_width = self.island_shore)
            self.canvas.draw_text(text = island_name, location = (x, y+3), color=helper.ISLAND_NAME_TEXT_COLOR, font=None, angle=0, text_location=helper.CENTER)

    def draw_ship(self) -> None: 
        # ship has sail_shape and hull_shape. 
        # these are already writen to return as centered around the correct island's dock_x_y
        for each_sail_shape in self.world.ship.sail_shape: 
            self.canvas.draw_polygon(
                points = each_sail_shape, fill_color = helper.SHIP_SAIL_FILL, 
                line_color = helper.SHIP_SAIL_LINE, line_width = 2)
        for each_hull_shape in self.world.ship.hull_shape: 
            self.canvas.draw_polygon(
                points = each_hull_shape, fill_color = helper.SHIP_HULL_FILL, 
                line_color = helper.SHIP_HULL_LINE, line_width = 2)
        pass

    


class HandOfGod():

    def __init__(self, window, world, best_1_canvas, best_path_canvas = None) -> None:
        self.window = window
        self.world = world
        self.best_1_out_mapper = Cartographer(world, best_1_canvas, helper.BEST_1_OUT_GRAPH_KEY)
        self.best_long_path_mapper = Cartographer(world, best_path_canvas, helper.BEST_LONG_PATH_GRAPH_KEY)
        self.values = None

    def get_selected_island(self, name_only  = True) -> str:
        if debug: print(f"get_selected_island {name_only=}" )
        name = self.values[helper.SELECT_ISLAND_NAME_KEY] 
        if debug: print(f"get_selected_island_name {name=} {name_only=}")
        if name == helper.SELECT_ISLAND_NAME_PRMOPT:
            return None
        else:
            if name_only:
                return name
            else: 
                return self.world.island_holder[name]

    def process_event_input(self, event, values) -> None: # exit is handled in the while
        self.set_values(values)
        match event: 
            case event_ if helper.WORLD_MODE_KEY in event_: 
                self.update_world_mode(event)
            case helper.AUTO_POPULATE_BUY_KEY:
                self.left_overs_into_other(helper.BUY_ITEM)
            case helper.AUTO_POPULATE_SELL_KEY:
                self.left_overs_into_other(helper.SELL_ITEM)
            case helper.BEST_LONG_PATH_BUTTON_KEY:
                self.populate_long_path_tab()
            case helper.CLEAR_SELECTED_ISLAND | helper.CLEAR_BAG_BUTTON_KEY :
                self.clear_only_selected_island()
            case helper.CLEAR_ALL_ISLANDS:
                self.clear_all_islands_bags()
            case helper.REMOVE_ITEM_BUTTON_KEY:
                self.remove_item()
            case helper.ISLAND_SELECTED_BUTTON_KEY:
                self.update_selected_island()
            case helper.TRAVEL_ISLAND_BUTTON_KEY:
                self.travel_to()
            case helper.UPDATE_BAG_BUTTON_KEY:
                self.send_bags_to_py()
            case helper.UPDATE_SHIP_KEY:
                self.ship_update_values()
            case helper.SAVE_ENTRIES:
                self.save_triggered()

    def clear_all_islands_bags(self) -> None:
        if debug: print(f"clear_all_islands_bags")
        self.world.reset_all_island_bags()
        self.refresh_dispaly()
        self.send_confirmation(f"Buy/Sell for all islands cleared.")

    def clear_only_selected_island(self) -> None:
        if debug: print(f"clear_only_selected_island:")
        island_py = self.get_selected_island(name_only=False)
        if island_py == None:
            return
        island_py.reset_bags()
        self.refresh_dispaly()
        self.send_confirmation(f"Buy/Sell for {island_py.name} cleared.")

    def draw_map(self, selection = helper.BEST_1_OUT_GRAPH_KEY, table = None ) -> None:
        if table == None:
            table = self.world.best_outbound_trades.values.tolist()
        if selection == helper.BEST_1_OUT_GRAPH_KEY:
            self.best_1_out_mapper.draw_map(table)
        elif selection == helper.BEST_LONG_PATH_GRAPH_KEY:
            self.best_long_path_mapper.draw_map(table)
        else:
            return 

    def left_overs_into_other(self, empty_bag) -> None:
        if debug: print(f"left_overs_into_other {empty_bag=}")
        island_py = self.get_selected_island(name_only=False)
        if island_py == None:
            return # no island selected to move stuff
        self.send_bags_to_py()  # fill island bags with current selections
        island_py = self.get_selected_island(name_only=False)
        island_py.left_overs_into_other_bag(empty_bag)
        self.refresh_dispaly()
        self.send_confirmation(f"{island_py.name}'s full bag used to fill {empty_bag} bag.")

    def populate_ship_connections(self) -> None:
        if debug: print(f"populate_ship_connections")
        self.window[helper.SHIP_TRADE_TABLE_KEY].update([values[1:] for values in self.world.trade_from_single_island().values.tolist()])

    def populate_bag_column(self, selected_island_py) -> None:
        if debug: print(f"populate_bag_column: {selected_island_py.name = }")
        self.window[helper.SELECTED_ISLAND_NAME_DISPLAY_KEY].update(f"{helper.SELECTED_HEADER_PREFIX} {selected_island_py.name}")  # update onscreen display
        self.populate_bag_column_details(selected_island_py, helper.SELL_ITEM)
        self.populate_bag_column_details(selected_island_py, helper.BUY_ITEM)

    def populate_bag_column_details(self, selected_island_py, buyvssell) -> None:
        if debug: print(f"populate_bag_column_details: {selected_island_py.name = } {buyvssell}")
        if buyvssell == helper.BUY_ITEM:
            bag_in_use = selected_island_py.buy
        else:
            bag_in_use = selected_island_py.sell
        dict_in_use = list(bag_in_use.items())
        for index_num in range(6):    
            if index_num >= len(dict_in_use):
                item_name = item_mod = helper.BLANK
                item_value = "?"
            else:
                item_py, item_mod = dict_in_use[index_num]
                item_name = item_py.name
                item_value = bag_in_use.item_modded_value(item_py)

            self.window[helper.SELECTED_ITEM_KEY+buyvssell+str(index_num)].update(value=item_name)
            self.window[helper.SELECTED_ITEM_MOD_KEY+buyvssell+str(index_num)].update(value=item_mod)
            self.window[helper.DISPLAY_ITEM_VALUE+buyvssell+str(index_num)].update(value=item_value)

    def populate_long_path_tab(self):
        if debug: print("populate_long_path_tab A")
        table_data = self.world.best_long_path.values.tolist()
        if debug: print(table_data)
        if debug: print("populate_long_path_tab C")
        self.window[helper.BEST_LONG_PATH_TABLE_KEY].update(table_data)
        if debug: print("populate_long_path_tab D")
        self.draw_map(helper.BEST_LONG_PATH_GRAPH_KEY, table_data)
        if debug: print("populate_long_path_tab E")
        self.send_confirmation("Population of Best Long Path Complete")
        if debug: print("populate_long_path_tab F")

    def remove_item(self):
        island_py = self.get_selected_island(name_only=False)
        item = self.values[helper.REMOVE_ITEM_KEY] 
        island_py.remove_item(item)
        self.window[helper.REMOVE_ITEM_KEY].update(value=helper.BLANK)
        self.refresh_dispaly()
        self.send_confirmation(f"Item removed from {island_py.name}")

    def send_confirmation(self, text) -> None:
        text = helper.FOOTER_TEXT_PREFIX + text
        if debug: print(f"send_confirmation({text = })")
        self.window[helper.FOOTER_TEXT].update(value=text)

    def send_each_bag_to_py(self, island_name, buyvsell) -> None:
            if debug: print(f"send_bags_to_py > send_each_bag_to_py ({buyvsell})")
            for index_num in range(6):
                item_name = self.values[helper.SELECTED_ITEM_KEY+buyvsell+str(index_num)] 
                mod = self.values[helper.SELECTED_ITEM_MOD_KEY+buyvsell+str(index_num)] 
                if debug: print(f"{index_num = } {item_name = } {mod = }")
                if item_name not in (helper.BLANK, ""):
                    self.world.process_island_item_update(island_name, buyvsell, item_name, mod)
  
    def send_bags_to_py(self) -> None:
        if debug: print(f"send_bags_to_py")
        island_py = self.get_selected_island(name_only=False)
        self.send_each_bag_to_py(island_py, helper.SELL_ITEM)
        self.send_each_bag_to_py(island_py, helper.BUY_ITEM)
        self.refresh_dispaly()
        self.send_confirmation(f"{island_py.name} Bags Updated.")

    def set_values(self, values) -> None:
        self.values = values

    def ship_update_values(self) -> None:
        if debug: print(f"ship_update_values")
        self.send_ship_update_capacity()
        self.send_ship_update_bargain()
        self.refresh_dispaly()
        self.send_confirmation(f"Update to ship successful.")

    def send_ship_update_bargain(self) -> None:
        focus_value = self.values[helper.SHIP_BARGAINING_INPUT]
        if debug: print(f'{self.world.ship.bargaining_power_pct = }')
        try:
            focus_value = int(focus_value.replace("%",""))
        except:
            sg.popup_error(f"-- {focus_value} is an Invalid Entry for {helper.BARGAINING_POWER} -- \nPlease enter bargaining value as only whole numbers, or a whole number followed by a %. \n Examples: '5' or '5%'")
        else:  # try was successful
            if focus_value < 0:
                self.__error_negative_value_popup(focus_value=focus_value, focus_name=helper.BARGAINING_POWER)
            else:            
                self.world.ship.set_bargaining_power(focus_value)
        self.window[helper.SHIP_BARGAINING_INPUT].update(value= str(self.world.ship.bargaining_power_pct)+'%') # useful if # used without % or if an invalid text had been entered
        if debug: print(f'{self.world.ship.bargaining_power_pct = }')
        
    def send_ship_update_capacity(self) -> None:
        focus_value = self.values[helper.SHIP_CAPASITY_INPUT]
        if debug: print(f'{self.world.ship.capacity = } {focus_value}')
        try:
            focus_value = int(focus_value)
        except:
            sg.popup_error(f"-- {focus_value} is an Invalid Entry for [{helper.CAPACITY}] -- \nPlease enter new value as only whole numbers. \n Example: '150'")
            self.window[helper.SHIP_CAPASITY_INPUT].update(value= str(self.world.ship.capacity)) # useful if an invalid text had been entered
        else:  # try was successful
            if focus_value < 0:
                self.__error_negative_value_popup(focus_value=focus_value, focus_name=helper.CAPACITY)
            else:
                self.world.ship.set_capacity(focus_value)
        if debug: print(f'{self.world.ship.capacity = }')

    def send_ship_update_travel_points(self) -> None:  # was removed as this ended up not being used in the recursive calculation
        focus_value = self.values[helper.TRAVEL_POINTS_INPUT]
        if debug: print(f"send_ship_travel_points {focus_value=}")
        try:
            focus_value = int(focus_value)
        except:
            sg.popup_error(f"-- {focus_value} is an Invalid Entry for {helper.TRAVEL_POINTS} -- \nPlease enter new value as only whole numbers. \n Example: '9'")
        else: 
            if focus_value < 0:
                self.__error_negative_value_popup(focus_value=focus_value, focus_name=helper.TRAVEL_POINTS)
            else:
                self.world.ship.travel_points = focus_value
        if debug: print(f"{self.world.ship.travel_points=}")

    def __error_negative_value_popup(self, focus_value, focus_name) -> None:
        sg.popup_error(f"-- {focus_value} is an Invalid Entry for {focus_name} -- \nPlease enter new value that is 0 greater. \n Example: '9'")

    def travel_to(self) -> None:
        next_island = self.values[helper.TRAVEL_ISLAND_NAME_KEY]  # self.window[helper.TRAVEL_ISLAND_NAME_KEY].get()
        if next_island == helper.TRAVEL_ISLAND_NAME_PRMOPT:
            return
        island_py = self.world.island_holder[next_island]
        if debug: print(f"travel_to: {next_island}")
        self.world.ship.set_location(island_py)
        self.window[helper.CONNECTIONS_TABLE_TITLE_KEY].update(helper.CONNECTIONS.format(next_island))
        self.window[helper.LOCATION_KEY].update(helper.LOCATION.format(next_island))
        self.refresh_dispaly()
        self.send_confirmation(f"Traveled to {next_island}.")
        
    def update_center(self) -> None:
        if debug: print("udpate center")
        self.update_center_trade_table()
        self.draw_map()

    def update_center_trade_table(self) -> None:
        if debug: print("update_center_trade_table")
        try: # fails when data has been cleared, but no new data has yet been entered
            self.window[helper.BEST_1_OUT_TABLE_KEY].update(self.world.best_outbound_trades.values.tolist())
        except: 
            self.window[helper.BEST_1_OUT_TABLE_KEY].update([[helper.BLANK,helper.BLANK,helper.BLANK,helper.BLANK]])
            pass

    def update_selected_island(self) -> None:
        if debug: print("update_selected_island")
        selected_island_py = self.get_selected_island(name_only=False)
        if selected_island_py == None: 
            # hide bag edit area
            self.window[helper.SELL_ITEM+helper.FRAME_KEY].update(visible=False)
            self.window[helper.BUY_ITEM+helper.FRAME_KEY].update(visible=False)
            self.window[helper.REMOVE+helper.FRAME_KEY].update(visible=False)
            return
        else:
            # show bag edit area
            self.window[helper.BUY_ITEM+helper.FRAME_KEY].update(visible=True)
            self.window[helper.SELL_ITEM+helper.FRAME_KEY].update(visible=True)
            self.window[helper.REMOVE+helper.FRAME_KEY].update(visible=True)
            self.populate_bag_column(selected_island_py)
        self.send_confirmation(f'Island of {selected_island_py.name} selected.')

    def update_world_mode(self, text):
        if debug: print(f"update_world_mode {text}")
        # pull value from text
        text = text.replace(helper.WORLD_MODE_KEY,"")
        self.world.set_mode(text)
        self.refresh_dispaly()
        self.send_confirmation(f"Mode updated to {text}")

    def save_triggered(self) -> None:
        if debug: print('save_triggered')
        chosen = sg.popup_yes_no('Would you like to save?', title= 'Save?')
        if debug: print (f"save_triggered {chosen = }")
        if chosen == helper.YES:
            self.world.save_all()
            self.send_confirmation("Save Comand Sent")
        else:
            self.send_confirmation("Not saved")
            pass

    def refresh_dispaly(self)-> None:
        if debug: print(f"refresh_dispaly")
        self.world.populate_trade_data()
        self.update_center()
        self.populate_ship_connections() # is there any time the ship isn't at an island? 
        self.update_selected_island()
        pass