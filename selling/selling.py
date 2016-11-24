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

        ui.print_menu("Accounting menu", options, "Back")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            remove(table, id_)
        elif option == "4":
            update(table, id_)
        elif option == "5":
            get_lowest_price_item_id(table)
        elif option == "6":
            get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        return


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    title_list = ["id", "title", "price", "day", "month", "year"]
    ui.print_table(table, title_list)
    start_module()


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    min = table[0][2]
    my_list = []
    counter = 0
    for row in range(len(table)):
        if table[row][2] < min:
            min = table[row][2]
            my_list.append(table[row])
    n = len(my_list)
    while n > 1:
        n -= 1
        for row in range(len(my_list) - 1):
            if my_list[row][1].lower() > my_list[row + 1][1].lower():
                my_list[row], my_list[row + 1] = my_list[row + 1], my_list[row]

    return my_list[0][0]


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    my_list = []
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
    for row in range(len(table)):
        if len(table[row][3]) != 2:
            table[row][3] = "0" + str(table[row][3])
        if len(table[row][4]) != 2:
            table[row][4] = "0" + str(table[row][4])
    for row in range(len(table)):
        date = table[row][5] + table[row][3] + table[row][4]
        if date > from_data and date < to_data:
            my_list.append(table[row])
    for row in range(len(my_list)):
        my_list[row][5] = int(my_list[row][5])
        my_list[row][3] = int(my_list[row][3])
        my_list[row][4] = int(my_list[row][4])
        my_list[row][2] = int(my_list[row][2])
    return my_list
