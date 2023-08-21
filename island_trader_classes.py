import json 
import pandas

debug = False


class Json_file_Manager(): 
    DEFAULT_FILE = "detault_data.json"
    SAVE_FILE = "saved_info.json" 
    ENVIRONMENT_FOLDER = "Bloodline_Hearos_of_Lithas\\"
    # so this will get the JSON object (or parts of it) from the file 
    # and send any modifications to the file 
    def __init__(self) -> None:
        pass

    @classmethod
    def __file_exists_check(cls, func):
        # idea for a decorator, but can't get decorators to stack with @classmethod yet
        # if file NOT found
            # make a copy of defualt and give it the save name
        return func 
    
    @classmethod
    def clear_save_file(cls) -> None:
        # just replace save file with default?
        pass

    @classmethod
    def __get_file_content(cls):
        if debug: print(f'Json_file_Manager.__get_file_content')
        try: # because Visual Studio code is breaking my heart
            with open(cls.SAVE_FILE, 'r') as file:
                return json.load(file)
        except:
            save_file = cls.ENVIRONMENT_FOLDER + cls.SAVE_FILE
            with open(save_file, 'r') as file:
                return json.load(file)

    @classmethod 
    def __set_file_content(cls, new_dict_content) -> None:
        if debug: print(f'Json_file_Manager.set_file_content: {new_dict_content= }')
        try: # because Visual Studio code is breaking my heart
            with open(Json_file_Manager.SAVE_FILE, "w") as file:
                file.write(json.dumps(new_dict_content))
        except: 
            save_file = cls.ENVIRONMENT_FOLDER + cls.SAVE_FILE
            with open(save_file, "w") as file:
                file.write(json.dumps(new_dict_content))

    @classmethod
    def get_primary_object(cls, primary):
        if debug: print(f'Json_file_Manager.get_primary_object: {primary= }')  # debug
        return cls.__get_file_content()[primary]

    @classmethod
    def get_secondary_object(cls, primary, secondary):
        if debug: print(f'Json_file_Manager.get_secondary_object: {primary= } {secondary= }')  # debug
        object1 = cls.get_primary_object(primary)
        # print(object1)
        try:
            return object1[secondary]
        except:
            for each in object1:
                if each["name"] == secondary:
                    return each

    @classmethod
    def save_game(cls, world) -> None:
        if debug: print("Json_file_Manager.save_game: Start")
        # get current save data
        full_dict = cls.__get_file_content()
        # update ship stats
        full_dict = cls.__add_ship_to_save_data(full_dict, world.ship)
        # for each island, update each bag
        for island_py in world.island_holder.values():
            full_dict = cls.__add_one_island_to_save_data(full_dict, island_py)
        # sent updated data to file
        if debug: print(f"{len(full_dict) = }")
        cls.__set_file_content(full_dict)
        if debug: print("Json_file_Manager.save_game: Done")

    @classmethod
    def __add_ship_to_save_data(cls, full_dict, ship_py) -> dict : 
        if debug: print(f"Json_file_Manager.__add_ship_to_save_data")
        full_dict[ship_py.PRIMARY_KEY][ship_py.LOCATION_KEY]   = ship_py.current_location.name
        full_dict[ship_py.PRIMARY_KEY][ship_py.CAPACITY_KEY]   = ship_py.capacity
        full_dict[ship_py.PRIMARY_KEY][ship_py.BARGAINING_KEY] = ship_py.bargaining_power_pct
        return full_dict

    @classmethod
    def __add_one_island_to_save_data(cls, full_dict, island_py) -> dict:
        if debug: print(f"Json_file_Manager.__add_one_island_to_save_data {island_py.name}")
        full_dict[island_py.PRIMARY_KEY][island_py.name][island_py.SELLING_KEY] = dict(zip([str(item) for item in island_py.sell.keys()], island_py.sell.values()))
        full_dict[island_py.PRIMARY_KEY][island_py.name][island_py.BUYING_KEY]  = dict(zip([str(item) for item in island_py.buy.keys()],  island_py.buy.values()))
        return full_dict
  

class Item():
    PRIMARY_KEY = "items"
    
    def __init__(self, dict_obj) -> None:
        self.name = dict_obj["name"].title()
        self.value = dict_obj["base_value"]
        self.weight = dict_obj["weight"]

    def __repr__(self) -> str:
        return f"Item: {self.name, self.value, self.weight}"
        
    def __str__(self) -> str:
        return self.name


class Item_Bag(dict):
    item_modifier_keys = {'++': 30, '+': 15, 0: 0, '-': -15, '--': -30}   
    SELLING_KEY = "selling"
    BUYING_KEY = "buying"

    def __init__(self, type_key, dict_objs = [], world = None) -> None:
        self.mode = type_key
        self.bag_modifier = -1 if type_key == self.BUYING_KEY else 1  # buying takes away from purse, selling adds to it
        self.world = world
        for item_name, mod in dict_objs.items():
            self.__add_item_from_json(item_name, mod)
        
    def reset(self) -> None:
        self.clear()  # self is based off of dict()

    def __add_item_from_json(self, item_name, mod) -> None:
        py_item = self.world.item_holder[item_name]
        self.update({py_item: mod})

    def add_item(self, py_item, mod) -> None:
        self.update({py_item: mod})

    def item_modded_value(self, py_item):
        mod = self.item_modifier_keys.get(self[py_item], 0)
        # bargaining power only helps with buying cost, not selling profit
        if self.mode == self.BUYING_KEY : 
            mod -= self.world.ship.bargaining_power_pct # bargaining power reduces inflation
        value_adjustment = (((py_item.value) * (mod))//100 )
        return int(py_item.value + value_adjustment)  * self.bag_modifier
    
    def remove_item(self, py_item):
        if py_item in self:
            self.pop(py_item)

    def __repr__(self):
        return f"Item_Bag: {self.mode} {[each for each in self.items()]}"


class Island():
    PRIMARY_KEY = "nodes"
    SELLING_KEY = Item_Bag.SELLING_KEY
    BUYING_KEY = Item_Bag.BUYING_KEY
    LOCATION_KEY = "loc_x_y"
    SHAPE_KEY = "shape"
    DOCK_KEY = "dock_x_y"

    def __init__(self, world, island_name, dict_obj) -> None:
        self.world = world
        self.name = island_name.title()
        self.links = dict()  # linked island: weight
        self.sell = Item_Bag(type_key = self.SELLING_KEY, dict_objs = dict_obj[self.SELLING_KEY], world = world)
        self.buy = Item_Bag(type_key = self.BUYING_KEY, dict_objs = dict_obj[self.BUYING_KEY], world = world)
        self.loc_x_y = tuple(dict_obj[self.LOCATION_KEY])
        self.shape = self.shifted_shape(dict_obj[self.SHAPE_KEY])
        self.dock = self.__x_y_shift(dict_obj[self.DOCK_KEY])
        
    @property
    def __link_count(self):
        # if debug: print("__link_count")
        return len(self.links)
    
    @property
    def x(self):
        return self.loc_x_y[0]
    
    @property
    def y(self):
        return self.loc_x_y[1]
    
    def __x_y_shift(self, point: list or tuple) -> tuple:
        return (point[0]+self.x, point[1]+self.y)

    def shifted_shape(self, shape_array) -> list:
        if shape_array == None:
            return None
        for index, each_pair in enumerate(shape_array):
            shape_array[index] = self.__x_y_shift(each_pair)
        return shape_array

    def reset_bags(self):
        if debug: print(f"reset_bags {self.name}")
        self.buy.reset()
        self.sell.reset()
    
    def remove_item(self, item):
        if type(item) == str:  # item will often be string
            item = self.world.item_holder[item]
        self.sell.remove_item(item)
        self.buy.remove_item(item)

    def all_outgoing_trades(self): 
        trade_rows = list()
        for each_island in list(self.links.keys()):
            trade_rows += self.__outgoing_trades_to_one(each_island)
        return trade_rows

    def __outgoing_trades_to_one(self, destination_island_py):
        trade_rows = list()
        tradable_items = set(self.buy).intersection(set(destination_island_py.sell))             
        for current_item in tradable_items:
            values = self.__item_cost_revenue_income(destination_island_py, current_item)
            weight = self.links[destination_island_py]
            trade_rows.append([self.name, destination_island_py.name, current_item.name] + values + [weight, int(values[1]/weight)])
        return trade_rows


    def __item_cost_revenue_income(self, destination_island, py_item: Item) -> list: 
        purchase_cost = self.buy.item_modded_value(py_item) * self.world.ship.most_can_carry(py_item)
        revenue = destination_island.sell.item_modded_value(py_item) * self.world.ship.most_can_carry(py_item)
        income = purchase_cost + revenue
        return [purchase_cost, revenue, income ]
    
    def add_item(self, buyvsell, py_item, mod):
        if debug: print(f"island.add_item {buyvsell = } {py_item = } {mod =}")
        if buyvsell == 'b':
            self.add_buy_item(py_item, mod)
        elif buyvsell == 's':
            self.add_sell_item(py_item, mod)
        else:
            print(f"error, {buyvsell = } invalid")

    def add_sell_item(self, py_item, mod): 
        if debug: print(f"add_sell_item {py_item =} {mod=}")
        self.buy.remove_item(py_item)  # protects items from being on both lists 
        self.sell.add_item(py_item, mod)

    def add_buy_item(self, py_item, mod):
        if debug: print(f"add_buy_item {py_item =} {mod=}")
        self.sell.remove_item(py_item) # protects items from being on both lists 
        self.buy.add_item(py_item, mod)

    def left_overs_into_other_bag(self, empty_) -> None:
        if debug: print(f"left_overs_into_other_bag({self.name} {empty_})")
        if empty_[0].lower() == 'b': 
            full_bag =  self.sell  # sell bag has items
            empty_bag = self.buy  # buy bag needs items
        else:
            full_bag = self.buy # buy bag has items
            empty_bag = self.sell  # sell bag is empty
        for item in self.world.item_holder.values():
            if item not in full_bag:
                mod = empty_bag.get(item, "")  # incase the "empty_bag" has some items populated in it
                empty_bag.add_item(item, mod)   

    def add_link(self, linking_island, weight) -> None: 
        if debug: print("add_link")
        self.links.update({linking_island: weight})

    def __repr__(self) -> str:
        return f"{self.name} x {self.__link_count}"


class Ship():
    PRIMARY_KEY = "ship"
    LOCATION_KEY = "current_location"
    CAPACITY_KEY = "capacity"
    BARGAINING_KEY = "bargaining_power"
    SAIL_KEY = "ship_sail"
    HULL_KEY = 'ship_hull'

    def __init__(self, world) -> None:
        dict_obj = Json_file_Manager.get_primary_object(self.PRIMARY_KEY)
        self.world = world
        self.current_location = world.island_holder[dict_obj[self.LOCATION_KEY]]  # Island object
        self.capacity = dict_obj[self.CAPACITY_KEY]
        self.bargaining_power_pct = dict_obj[self.BARGAINING_KEY] # bargaining power only helps with buying cost, not selling profit
        self.travel_points = 10
        self.__sail_shape = dict_obj[self.SAIL_KEY]
        self.__hull_shape = dict_obj[self.HULL_KEY]  
            # when ready to use : self.current_location.shifted_shape(dict_obj[self.HULL_KEY] )
       
    @property
    def sail_shape(self):
        return self.current_location.shifted_shape(self.__sail_shape)

    @property
    def hull_shape(self):
        return self.current_location.shifted_shape(self.__hull_shape)

    def set_location(self, new_island) -> None:
        try:
            if type(new_island) == str:
                new_island = self.world.island_holder[new_island]
            if type(new_island) == Island:
                self.current_location = new_island
        except: 
            print(f"Error: {new_island} does not seem to be a valid entry - location not updated")

    def set_capacity(self, new_capacity: int) -> None:
        self.capacity = new_capacity

    def set_bargaining_power(self, new_bargaining_power: int) -> None:
        self.bargaining_power_pct = new_bargaining_power

    def most_can_carry(self, py_item) -> int:
        return self.capacity // py_item.weight

    def item_profit(self, source_island: Island, destination_island: Island, py_item: Item) -> int: 
        purchase_cost = source_island.buy.item_modded_value(py_item, self)
        selling_value = destination_island.sell.item_modded_value(py_item, self)
        profit_1 = purchase_cost + selling_value
        quantity = self.most_can_carry(py_item)
        return int(quantity * profit_1)


class World():
    NO_MATCH = 'no match'
    FROM = 'From'
    TO = 'To'
    ITEM = 'Item' 
    COST = 'Item Cost'  # expence to get item
    INCOME = 'Income'  # Income, on the other hand, is the total amount of money earned after all expenses are deducted
    REVENUE = 'Revenue'  # Revenue is the total amount of money an entity earns from a variety of sources
    MOVEMENT = "MoveC"
    REVENUE_PER_MC = "Revenue/MC"
    VALUES = "Values"
    POSIBLE_MODES = [REVENUE, INCOME, REVENUE_PER_MC]
    df_full_headers = [FROM, TO, ITEM, COST, REVENUE, INCOME, MOVEMENT, REVENUE_PER_MC]
    
    def __init__(self) -> None:
        print("Generating World...")
        self.item_holder = dict()
        self.island_holder = dict() 
        self.last_island_name = None
        self.mode = self.REVENUE_PER_MC  # focus value for calculations        
        self.__populate_item_holder() 
        self.__populate_island_holder() # island referance item_holder
        self.__populate_island_links()
        self.ship = Ship(self)  # ship referances island_holdder
        self.trade_dataframe = None
        self.populate_trade_data()
        self.__long_path_holder = [[0, 0]]

    def __populate_item_holder(self) -> None:
        if debug: print("populate_item_holder")
        for item_dict in Json_file_Manager.get_primary_object("items"):
            self.item_holder.update({item_dict['name'].title(): Item(item_dict)})

    def __populate_island_holder(self) -> None:
        if debug: print("populate_island_holder")
        for island_name, island_dict in Json_file_Manager.get_primary_object(Island.PRIMARY_KEY).items():
            self.island_holder.update({island_name.title(): Island(self, island_name, island_dict)})
            self.last_island_name = island_name.title() # order maters, last island is center
        
    def __populate_island_links(self) -> None:
        for u_edge in Json_file_Manager.get_secondary_object("edges", "undirected edges"):
            island_0, island_1 = u_edge["nodes"]
            island_0 = self.island_holder[island_0]
            island_1 = self.island_holder[island_1]
            weight = u_edge["weight"]
            island_0.add_link(island_1, weight)
            island_1.add_link(island_0, weight)
        return
        for d_edge in Json_file_Manager.get_secondary_object("edges", "directed edges"):  # only included as a graphing exersize
            island_from = self.island_holder[d_edge["from"]]
            island_to =   self.island_holder[d_edge["to"]]
            weight = d_edge["weight"]
            island_from.add_link(island_to, weight)

    def process_island_item_update(self, island_py: Island, buyvsell:str, item_name:str, mod:str) -> None :
        if debug: print(f"World.process_island_item_update {island_py.name, buyvsell, item_name, mod}")
        buyvsell = buyvsell[0].lower()  # adjust for formating differances between this class and viewer
        if item_name not in self.item_holder:
            return
        py_item = self.item_holder[item_name]
        island_py.add_item(buyvsell, py_item, mod)
        return

    def reset_all_island_bags(self) -> None:
        for each_island in self.island_holder:
            each_island = self.island_holder[each_island]
            each_island.reset_bags()
      
    def save_all(self):  #
        if debug: print("World.save_all")
        Json_file_Manager.save_game(self)

    def populate_trade_data(self):
        if debug: print(f"World.populate_trade_data")
        data = list()
        for from_island in self.island_holder.values():
            data += from_island.all_outgoing_trades()
        # return data
        self.trade_dataframe = pandas.DataFrame(data, columns=self.df_full_headers).sort_values(by=[self.mode], ascending=False)
        self.trade_dataframe.fillna(-10000000)
        if debug: print(self.trade_dataframe)

    def trade_from_single_island(self, focus_island: Island = None) -> pandas.DataFrame:
        if focus_island == None:
            focus_island = self.ship.current_location
        if type(focus_island) == Island:  # display call will likely send str instead of Island
            focus_island = focus_island.name
        return self.trade_dataframe.query(f'{self.FROM} == "{focus_island}"')
    
    def set_mode(self, new_mode) -> None:
        if new_mode not in self.POSIBLE_MODES:
            return 
        else:
            self.mode = new_mode
    
    @property
    def best_outbound_trades(self ) -> pandas.DataFrame:
        mode_headers = [self.FROM, self.TO, self.ITEM, self.mode]
        try: 
            data = list()
            focus_list = self.trade_dataframe[[self.FROM, self.mode]].groupby([self.FROM], as_index=False).max([self.mode]).values.tolist()
            for from_island, max_value in focus_list:
                data += self.trade_dataframe[(self.trade_dataframe[self.FROM] == from_island) & (self.trade_dataframe[self.mode] == max_value)][mode_headers].values.tolist()
            data_frame = pandas.DataFrame(data, columns=mode_headers).sort_values([self.mode], ascending= False)
            return data_frame.rename(columns={self.mode: self.VALUES})
        except:
            return self.trade_dataframe

    def __add_to_multi_holer(self, new_list, max_items = 1):
        new_value = new_list[0]
        current_minimum = self.__long_path_holder[-1][0]    
        if (len(self.__long_path_holder) == max_items) and (new_value <= current_minimum):
            return
        else:
            for index, current_item in enumerate(self.__long_path_holder): 
                current_value = current_item[0]
                if current_value < new_value:
                    self.__long_path_holder.insert(index, new_list)
                    break # done with current for loop
            
        if len(self.__long_path_holder) > max_items:
            a = self.__long_path_holder.pop(-1)

    @property
    def long_path_headers_panda(self):
        return [self.FROM, self.TO, self.ITEM, self.mode, self.MOVEMENT]
    
    @property
    def long_path_headers_display(self):
        return [self.FROM, self.TO, self.ITEM, self.VALUES, self.MOVEMENT]


    def __calculations_for_best_long_path(self, from_island_py: Island, remaining_movment_points: int, running_value = 0, running_path = [], indent = ""):
        if remaining_movment_points <= 0:  # send results of path to logger 
            # print(indent, f"I hit the base: {running_value=}, {running_path=}")
            self.__add_to_multi_holer([running_value] + running_path)
            # add path to multi_holder
            return
        for destination_island_py, movement_cost in from_island_py.links.items():
            # print(indent, "a", from_island_py, destination_island_py, movement_cost)
            if movement_cost > remaining_movment_points:
                # can not afford to move here
                # print(indent, f"Can't afford this trip: {from_island_py, '>', destination_island_py, movement_cost, remaining_movment_points}")
                self.__calculations_for_best_long_path(from_island_py, 0, running_value, running_path, indent + " " ) 
            else:
                filtered_df = self.trade_dataframe[self.long_path_headers_panda].query(
                    f"""{self.FROM} == "{from_island_py.name}" and {self.TO} == "{destination_island_py.name}" """
                    ).head(1)
                # print(indent, f"{filtered_df.shape=}")
                # print(indent, f"{filtered_df=}")
                if filtered_df.shape[0] < 1: # no match to filter found, this path is a dead end
                    # print(indent, f"No Match: {from_island_py, destination_island_py, movement_cost, remaining_movment_points}")
                    self.__calculations_for_best_long_path(from_island_py, 0, running_value, running_path, indent + " " )
                else: 
                    # print(indent, f"Making this trip: {from_island_py, destination_island_py, movement_cost, remaining_movment_points}")                
                    #   new_path_entry = [filtered_df.iloc[0][self.long_path_headers_panda].array.tolist()]
                    new_path_entry = [filtered_df.iloc[0].to_list()]
                    added_value = filtered_df[self.mode].to_list()[0]
                    # print(indent, f" {added_value=} {new_path_entry=}")
                    self.__calculations_for_best_long_path(destination_island_py, remaining_movment_points - movement_cost, running_value + added_value, running_path + new_path_entry , indent + " " )

    @property
    def best_long_path(self, steps = 8):
        # start of best loop can be no more than 2 steps away
        # gives 6 steps to travel loop - feed good for verifying high value.
        self.__long_path_holder = [[0, 0]]  # reset to hold new values
        try:
            self.__calculations_for_best_long_path(self.ship.current_location, steps)
        except:
            self.__add_to_multi_holer([1000000, ["A-best_long_path failed in some way", "B", "C", 4, 5]])
        temp_table = pandas.DataFrame(self.__long_path_holder[0][1:], columns=self.long_path_headers_panda)
        return temp_table.rename(columns={self.mode: self.VALUES})
    
    @property
    def best_long_path_dummy(self, steps = 8):
        temp_table = pandas.DataFrame([self.long_path_headers_panda], columns=self.long_path_headers_display)
        return temp_table.rename(columns={self.mode: self.VALUES})



