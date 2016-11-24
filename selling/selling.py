# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
    table = data_manager.get_table_from_file("selling/sellings.csv")

    while True:
        options = ["Print the default table of records",
                   "Add an item to the table",
                   "Remove from table",
                   "Update an item in the table",
                   "What is the id of the item that sold for the lowest price?",
                   "Which items are sold between two given dates?"]

        ui.print_menu("Sellings", options, "Back")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
            data_manager.write_table_to_file("accounting/items.csv", table)
        elif option == "3":
            id_ = ui.get_inputs(["Please enter an id to remove: "], "")
            remove(table, id_)
            data_manager.write_table_to_file("selling/sellings.csv", table)
        elif option == "4":
            id_ = ui.get_inputs(["Please enter an id to update: "], "")
            update(table, id_)
            data_manager.write_table_to_file("selling/sellings.csv", table)
        elif option == "5":
            label = "Id of the lowest sold item: "
            result = get_lowest_price_item_id(table)
            ui.print_result(result, label)
        elif option == "6":
            label = "Items are sold between two given dates: "
            list_labels = ["month from","day from","year from","month to","day to","year to"]
            input = ui.get_inputs(list_labels, "")
            result = get_items_sold_between(table, input[0], input[1], input[2], input[3], input[4], input[5])
            ui.print_result(result, label)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        return


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    title_list = ["id", "title", "price", "month", "day", "year"]
    ui.print_table(table, title_list)
    start_module()


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    id = common.generate_random(table)
    list_labels = ["title", "price", "month", "day", "year"]
    title = "Add item to list"
    inputs = []
    inputs = ui.get_inputs(list_labels, title)
    inputs.insert(0, id)
    table.append(inputs)
    
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

    list_labels = ["title", "price", "month", "day", "year"]
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

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    min_price = table[0][2]
    sorted_list = []
    counter = 0
    for row in table:
        price = row[2]
        if price < min_price:
            min_price = price
            sorted_list.append(row)
    lengt_of_list = len(sorted_list)
    while lengt_of_list > 1:
        lengt_of_list -= 1
        for row in range(len(sorted_list) - 1):
            if sorted_list[row][1].lower() > sorted_list[row + 1][1].lower():
                sorted_list[row], sorted_list[row + 1] = sorted_list[row + 1], sorted_list[row]

    return sorted_list[0][0]


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    filtered_table = []
    if len(str(month_from)) != 2:
        month_from = "0" + str(month_from)
    if len(str(month_to)) != 2:
        month_to = "0" + str(month_to)
    if len(str(day_from)) != 2:
        day_from = "0" + str(day_from)
    if len(str(day_to)) != 2:
        day_to = "0" + str(day_to)
    from_data = str(year_from) + str(month_from) + str(day_from)
    to_data = str(year_to) + str(month_to) + str(day_to)
    for row in table:
        month = row[3]
        day = row[4]
        if len(month) != 2:
            month = "0" + str(month)
        if len(day) != 2:
            day = "0" + str(day)
    for row in table:
        year = row[5]
        month = row[3]
        day = row[4]
        date = year + month + day
        if date > from_data and date < to_data:
            filtered_table.append(row)
    for row in filtered_table:
        row[5] = int(row[5])
        row[4] = int(row[3])
        row[3] = int(row[4])
        row[2] = int(row[2])

    return filtered_table
