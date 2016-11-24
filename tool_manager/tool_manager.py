# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    table = data_manager.get_table_from_file("tool_manager/tools.csv")

    while True:
        options = ["Print the default table of records",
                   "Add an item to the table",
                   "Remove from table",
                   "Update an item in the table",
                   "Which items has not yet exceeded their durability?",
                   "What are the average durability time for each manufacturer?"]

        ui.print_menu("Accounting menu", options, "Back")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            id_ = ui.get_inputs(["Please enter an id to remove: "], "")
            remove(table, id_)
            data_manager.write_table_to_file("tool_manager/tools.csv", table)
        elif option == "4":
            id_ = ui.get_inputs(["Please enter an id to remove: "], "")
            update(table, id_)
            data_manager.write_table_to_file("tool_manager/tools.csv", table)
        elif option == "5":
            get_available_tools(table)
        elif option == "6":
            get_average_durability_by_manufacturers(table)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        return


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    title_list = ["id", "name", "manufacturer", "purchase date", "durability"]
    ui.print_table(table, title_list)
    start_module()


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    id = common.generate_random(table)
    list_labels = ["name", "manufacturer", "purchase date", "durability"]
    title = "Add item to list"
    inputs = []
    inputs = ui.get_inputs(list_labels, title)
    inputs.insert(0, id)
    table.append(inputs)
    data_manager.write_table_to_file("tool_manager/tools.csv", table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    user_id = str(id_[0])
    for row in table:
        original_id = row[0]
        if original_id == user_id:
            table.remove(row)

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    list_labels = ["name", "manufacturer", "purchase date", "durability"]
    user_id = str(id_[0])
    for row in range(len(table)):
        original_id = table[row][0]
        if original_id == user_id:
            new_data = ui.get_inputs(list_labels,"Update data")
            new_data.insert(0, user_id)
            table[row]= new_data

    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    update_table = []
    for row in table:
        purchase_date = int(row[3])
        durability = int(row[4])
        result = purchase_date + durability
        if result > 2016:
            row[3] = int(row[3])
            row[4] = int(row[4])
            update_table.append(row)
    return update_table


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    my_dict = {}
    for row in table:
        sum_of_durability = 0
        result = 0
        counter = 0
        manufacture = row[2]
        for row in table:
            manufacture_2 = row[2]
            durability = int(row[4])
            if manufacture == manufacture_2:
                sum_of_durability += durability
                counter += 1
        average = sum_of_durability / counter
        my_dict.update({manufacture: average})
    return my_dict
