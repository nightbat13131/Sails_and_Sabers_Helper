import json 
import pandas
import common_strings as st
from copy import deepcopy
from tkinter.filedialog import askopenfile # open - import
from tkinter.filedialog import asksaveasfilename # save as - export
debug = False

class File_Manager(): 
    def __init__(self, world) -> None:
        self.file_path = None
        self.world = world

    def get_dict(self):
        return deepcopy(st.default_save_format)

    def __create_save_json(self) -> json: 
        if debug: print(f"File_Manager.__create_save_json")
        holder = self.get_dict()
        holder = self.__add_ship_to_save_data(holder)
        # for each island, update each bag
        for island_py in self.world.island_holder.values():
            holder = self.__add_one_island_to_save_data(holder, island_py)
        return json.dumps(holder)

    def save_as(self) -> bool:
        if debug: print(f"File_Manager.save_as")
        self.file_path = asksaveasfilename()
        print(self.file_path)
        return self.save()

    def save(self) -> bool:
        if debug: print(f"File_Manager.save")
        if self.file_path is None: 
            self.save_as()
        # open in write and replace? 
        save_content = self.__create_save_json()
        was_success = False
        try:
            with open(self.file_path, "w") as save_file:
                save_file.write(save_content)
            was_success = True
        except:
            print("Saving failed")
        return was_success
    
    def load(self) -> bool:
        if debug: print(f"File_Manager.load")
        was_successful = False
        try:
            loaded_file = askopenfile(title= "Choose .json to load")
            file_content = json.load(loaded_file)
            self.file_path = loaded_file.name
            loaded_file.close()
            self.world.ship.update_from_json(file_content[st.SHIP_PRIMARY_KEY])
            for island_name, dict_obj in file_content[st.ISLAND_PRIMARY_KEY].items():
                self.world.island_holder[island_name].update_from_json(dict_obj)
            was_successful = True
        except:
            print("Load failed")
        return was_successful
        
    def __add_ship_to_save_data(self, full_dict) -> dict : 
        if debug: print(f"File_Manager.__add_ship_to_save_data")
        full_dict[st.SHIP_PRIMARY_KEY][st.SHIP_LOCACTION_KEY]  = self.world.ship.current_location.name
        full_dict[st.SHIP_PRIMARY_KEY][st.SHIP_CAPACITY_KEY]   = self.world.ship.capacity
        full_dict[st.SHIP_PRIMARY_KEY][st.SHIP_BARGAINING_KEY] = self.world.ship.bargaining_power_pct
        return full_dict

    def __add_one_island_to_save_data(self, full_dict, island_py) -> dict:
        if debug: print(f"File_Manager.__add_one_island_to_save_data {island_py.name}")
        full_dict[st.ISLAND_PRIMARY_KEY][island_py.name][st.ISLAND_SELLING_KEY] = dict(zip([str(item) for item in island_py.sell.keys()], island_py.sell.values()))
        full_dict[st.ISLAND_PRIMARY_KEY][island_py.name][st.ISLAND_BUYING_KEY]  = dict(zip([str(item) for item in island_py.buy.keys()],  island_py.buy.values()))
        return full_dict   


class Item():
    
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

    def __init__(self, type_key, world = None) -> None:
        self.mode = type_key
        self.bag_modifier = -1 if type_key == st.ISLAND_BUYING_KEY else 1  # buying takes away from purse, selling adds to it
        self.world = world
        #for item_name, mod in dict_objs.items():
        #    self.__add_item_from_json(item_name, mod)
        
    def reset(self) -> None:
        self.clear()  # self is based off of dict()

    def add_item_from_json(self, item_name, mod) -> None:
        py_item = self.world.item_holder[item_name]
        self.update({py_item: mod})

    def add_item(self, py_item, mod) -> None:
        mod = mod if mod in self.item_modifier_keys.keys() else 0
        if len(self) >= 6:  # block more than 6 items being in the bag.
            if py_item in self:
                self[py_item] = mod  # update if pressent
            return
        self.update({py_item: mod})

    def item_modded_value(self, py_item):
        mod = self.item_modifier_keys.get(self[py_item], 0)
        # bargaining power only helps with buying cost, not selling profit
        if self.mode == st.ISLAND_BUYING_KEY : 
            mod -= self.world.ship.bargaining_power_pct # bargaining power reduces inflation
        value_adjustment = (((py_item.value) * (mod))//100 )
        return int(py_item.value + value_adjustment)  * self.bag_modifier
    
    def remove_item(self, item):
        if type(item) == str:  # item will often be string
            if item in self.world.item_holder: # protect against rouge strings
                item = self.world.item_holder[item]
        if item in self:
            self.pop(item)

    def __repr__(self):
        return f"Item_Bag: {self.mode} {[each for each in self.items()]}"


class Island():

    def __init__(self, world, island_name, dict_obj) -> None:
        self.world = world
        self.name = island_name.title()
        self.links = dict()  # linked island: weight
        self.sell = Item_Bag(type_key = st.ISLAND_SELLING_KEY, world = world)
        self.buy = Item_Bag(type_key = st.ISLAND_BUYING_KEY, world = world)
        self.loc_x_y = tuple(dict_obj[st.ISLAND_LOCATION_KEY])
        self.shapes = self.shifted_shape(dict_obj[st.ISLAND_SHAPE_KEY])
        self.dock = self.__x_y_shift_center(dict_obj[st.ISLAND_DOCK_KEY])
        
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
    
    def __x_y_shift_center(self, point: list or tuple) -> tuple:            
        if debug: print(point)
        return (point[0]+self.x, point[1]+self.y)

    def __x_y_shift_dock(self, point: list or tuple, focus = None) -> tuple: 
        if debug: print(point)
        x = self.dock[0]
        y = self.dock[1]
        return (point[0]+x, point[1]+y)

    def shifted_shape(self, shapes_array, mode = 'center') -> list:
        if debug: print("Island.shifted_shape", self.name, shapes_array )
        if shapes_array == None:
            return None
        for index_0, each_shape in enumerate(shapes_array):
            for index_1, each_pair in enumerate(each_shape):
                if mode == 'center':
                    shapes_array[index_0][index_1] = self.__x_y_shift_center(each_pair)
                else: 
                    shapes_array[index_0][index_1] = self.__x_y_shift_dock(each_pair)
        return shapes_array

    def reset_bags(self):
        if debug: print(f"reset_bags {self.name}")
        self.buy.reset()
        self.sell.reset()
    
    def remove_item(self, item):
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
    
    def update_from_json(self, dict_obj):
        if debug: print(f"Island.update_from_json: {dict_obj = }")
        self.reset_bags() # clear any items as this is an overwrite
        for item_name, mod in dict_obj[st.ISLAND_SELLING_KEY].items():
            self.sell.add_item_from_json(item_name, mod)
        for item_name, mod in dict_obj[st.ISLAND_BUYING_KEY].items():
            self.buy.add_item_from_json(item_name, mod)

    def add_item(self, buyvsell, py_item, mod):
        if debug: print(f"Island.island.add_item {buyvsell = } {py_item = } {mod =}")
        if buyvsell == st.ISLAND_BUYING_KEY[0]:
            self.add_buy_item(py_item, mod)
        elif buyvsell == st.ISLAND_SELLING_KEY[0]:
            self.add_sell_item(py_item, mod)
        else:
            print(f"error, {buyvsell = } invalid")

    def add_sell_item(self, py_item, mod): 
        if debug: print(f"Island.add_sell_item {py_item =} {mod=}")
        self.buy.remove_item(py_item)  # protects items from being on both lists 
        self.sell.add_item(py_item, mod)

    def add_buy_item(self, py_item, mod):
        if debug: print(f"Island.add_buy_item {py_item =} {mod=}")
        self.sell.remove_item(py_item) # protects items from being on both lists 
        self.buy.add_item(py_item, mod)

    def left_overs_into_other_bag(self, empty_) -> None:
        if debug: print(f"Island.left_overs_into_other_bag({self.name} {empty_})")
        if empty_[0].lower() == st.ISLAND_BUYING_KEY[0]: 
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
        if debug: print("Island.add_link")
        self.links.update({linking_island: weight})

    def __repr__(self) -> str:
        return f"{self.name} x {self.__link_count}"


class Ship():

    def __init__(self, world) -> None:
        self.world = world
        self.current_location = world.island_holder["Samalkan"]  # Island object
        self.capacity = 90
        self.bargaining_power_pct = 0 # bargaining power only helps with buying cost, not selling profit
        self.__sail_shape = st.ISLAND_DATA[st.SHIP_PRIMARY_KEY][st.SHIP_SAIL_KEY]
        self.__hull_shape = st.ISLAND_DATA[st.SHIP_PRIMARY_KEY][st.SHIP_HULL_KEY]  
        
    @property
    def sail_shape(self):
        safe_shape_array = deepcopy(self.__sail_shape)
        return self.current_location.shifted_shape(safe_shape_array, mode= 'dock')

    @property
    def hull_shape(self):
        safe_shape_array = deepcopy(self.__hull_shape)
        return self.current_location.shifted_shape(safe_shape_array, mode= 'dock')

    def update_from_json(self, dict_obj):
        if debug: print("Ship.update_from_json")
        self.current_location = self.world.island_holder[dict_obj[st.SHIP_LOCACTION_KEY]]
        self.capacity = dict_obj[st.SHIP_CAPACITY_KEY]
        self.bargaining_power_pct = dict_obj[st.SHIP_BARGAINING_KEY]

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
    FROM = '__From__'
    TO = '___To___'
    ITEM = '__Item__' 
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
        self.file_manager = File_Manager(self)

    def __populate_item_holder(self) -> None:
        if debug: print("World.__populate_item_holder")
        for item_dict in st.ISLAND_DATA[st.ITEM_PRIMARY_KEY]:
            self.item_holder.update({item_dict['name'].title(): Item(item_dict)})

    def __populate_island_holder(self) -> None:
        if debug: print("World.populate_island_holder")
        for island_name, island_dict in st.ISLAND_DATA[st.ISLAND_PRIMARY_KEY].items():  # worried about this DICT referance 
            self.island_holder.update({island_name.title(): Island(self, island_name, island_dict)})
            self.last_island_name = island_name.title() # order maters, last island is center
        
    def __populate_island_links(self) -> None:
        for u_edge in  st.ISLAND_DATA[st.ISLAND_EDGES_KEY][st.ISLAND_UNDIRECTED_KEY]: # Json_Manager.get_secondary_object("edges", "undirected edges"):
            island_0, island_1 = u_edge[st.ISLAND_PRIMARY_KEY]
            island_0 = self.island_holder[island_0]
            island_1 = self.island_holder[island_1]
            weight = u_edge["weight"]
            island_0.add_link(island_1, weight)
            island_1.add_link(island_0, weight)
        return

    def process_island_item_update(self, island_py: Island, buyvsell:str, item_name:str, mod:str) -> None :
        if debug: print(f"World.process_island_item_update {island_py.name, buyvsell, item_name, mod}")
        buyvsell = buyvsell[0].lower()  # adjust for formating differances between this class and viewer
        if item_name not in self.item_holder:
            return
        py_item = self.item_holder[item_name]
        island_py.add_item(buyvsell, py_item, mod)
        return

    def reset_all_island_bags(self) -> None:
        if debug: print(f"World.reset_all_island_bags")
        for each_island in self.island_holder:
            each_island = self.island_holder[each_island]
            each_island.reset_bags()

    def load(self)-> bool:
        if debug: print(f"World.load")
        was_successful = self.file_manager.load()
        if was_successful:
            self.populate_trade_data()
        return was_successful

    def save_as(self) -> bool:  #
        if debug: print("World.save_as")
        return self.file_manager.save_as()

    def save(self) -> bool:  #
        if debug: print("World.save")
        return self.file_manager.save()

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
        if debug: print(f"World.trade_from_single_island")
        if focus_island == None:
            focus_island = self.ship.current_location
        if type(focus_island) == Island:  # display call will likely send str instead of Island
            focus_island = focus_island.name
        return self.trade_dataframe.query(f'{self.FROM} == "{focus_island}"')
    
    def set_mode(self, new_mode) -> None:
        if debug: print(f"World.set_mode")
        if new_mode not in self.POSIBLE_MODES:
            return 
        else:
            self.mode = new_mode
    
    @property
    def best_outbound_trades(self ) -> pandas.DataFrame:
        if debug: print(f"World.best_outbound_trades @property")
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
        if debug: print(f"World.__add_to_multi_holer {new_list=}")
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
        if debug: print(f"{self.__long_path_holder}")
        if len(self.__long_path_holder) > max_items:
            a = self.__long_path_holder.pop(-1)

    @property
    def long_path_headers_panda(self):
        if debug: print(f"World.long_path_headers_panda @property")
        return [self.FROM, self.TO, self.ITEM, self.mode, self.MOVEMENT]
    
    @property
    def long_path_headers_display(self):
        if debug: print(f"World.long_path_headers_display @property")
        return [self.FROM, self.TO, self.ITEM, self.VALUES, self.MOVEMENT]

    def __calculations_for_best_long_path(self, from_island_py: Island, remaining_movment_points: int, running_value = 0, running_path = [], indent = ""):
        # no debug printout as this is recursive and printout will kill it.
        if remaining_movment_points <= 0:  # send results of path to logger 
            print(indent, f"I hit the base: {running_value=}, {running_path=}")
            self.__add_to_multi_holer([running_value] + running_path)
            return
        for destination_island_py, movement_cost in from_island_py.links.items():
            #print(indent, "a", from_island_py, destination_island_py, movement_cost)
            if movement_cost > remaining_movment_points: # can not afford to move here
                #print(indent, f"a.Can't afford this trip: {from_island_py, '>', destination_island_py, movement_cost, remaining_movment_points}")
                self.__calculations_for_best_long_path(from_island_py, 0, running_value, running_path, indent + " " ) 
            else:
                #print(indent, f"a.a {self.FROM} {from_island_py.name} {self.TO} {destination_island_py.name}")
                filtered_df = self.trade_dataframe[self.long_path_headers_panda].query(
                    f"""{self.FROM} == "{from_island_py.name}" and {self.TO} == "{destination_island_py.name}" """
                    ).head(1)
                #print(indent, f"a.b")
                #print(indent, f"{filtered_df.shape=}")
                #print(indent, f"{filtered_df=}")
                if filtered_df.shape[0] < 1: # no match to filter found, this path is a dead end
                    #print(indent, f"No Match: {from_island_py, destination_island_py, movement_cost, remaining_movment_points}")
                    self.__calculations_for_best_long_path(from_island_py, 0, running_value, running_path, indent + " " )
                else: 
                    #print(indent, f"Making this trip: {from_island_py, destination_island_py, movement_cost, remaining_movment_points}")                
                    new_path_entry = [filtered_df.iloc[0][self.long_path_headers_panda].array.tolist()]
                    new_path_entry = [filtered_df.iloc[0].to_list()]
                    added_value = filtered_df[self.mode].to_list()[0]
                    #print(indent, f" {added_value=} {new_path_entry=}")
                    self.__calculations_for_best_long_path(destination_island_py, remaining_movment_points - movement_cost, running_value + added_value, running_path + new_path_entry , indent + " " )

    @property
    def best_long_path(self, steps = 8):
            if debug: print(f"World.best_long_path")
            self.__long_path_holder = [[0, 0]]  # reset to prepare for new values
            if debug: print(f"World.best_long_path - pre call __calculations_for_best_long_path - entering try:")
        #try:
            self.__calculations_for_best_long_path(self.ship.current_location, steps)
            if debug: print(f"World.best_long_path - post call __calculations_for_best_long_path - success")
        #except:
        #    if debug: print("except: __calculations_for_best_long_path failed in some way")
        #finally:
            if debug: print(f"{self.__long_path_holder=}")
            if self.__long_path_holder ==  [[0, 0]]: # no change after having been reset
                return self.best_long_path_dummy
            temp_table = pandas.DataFrame(self.__long_path_holder[0][1:], columns=self.long_path_headers_panda)
            return temp_table.rename(columns={self.mode: self.VALUES})
    
    @property
    def best_long_path_dummy(self, steps = 8):
        if debug: print(f"World.best_long_path_dummy @property")
        temp_table = pandas.DataFrame([self.long_path_headers_panda], columns=self.long_path_headers_display)
        return temp_table.rename(columns={self.mode: self.VALUES})

       
