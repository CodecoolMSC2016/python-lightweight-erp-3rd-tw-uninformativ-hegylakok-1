# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
    table = data_manager.get_table_from_file("hr/persons.csv")

    while True:
        options = ["Print the default table of records",
                "Add an item to the table",
                "Remove from table",
                "Update an item in the table",
                "Who is the oldest person?",
                "Who is the closest to the average age?"]

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
            get_oldest_person(table)
        elif option == "6":
            get_persons_closest_to_average(table)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        return


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    title_list = ["id", "name", "birthdate"]
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

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    min = 2016
    my_list = []
    min_age = 0
    for row in range(len(table)):
        if int(table[row][2]) < min:
            min = int(table[row][2])
    for row in range(len(table)):
        if int(table[row][2]) == min:
            my_list.append(table[row][1])

    return my_list


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    checker = 0
    sum = 0
    my_list = []
    for row in range(len(table)):
        sum += 2016 - int(table[row][2])
        checker += 1
    average_age = sum / checker
    min = 100
    my_list = []
    for row in range(len(table)):
        result = (2016 - int(table[row][2])) - average_age
        if result < 0:
            result = result * -1
        if result < min:
            min = result
    for row in range(len(table)):
        result = (2016 - int(table[row][2])) - average_age
        if result < 0:
            result = result * -1
        if result == min:
            if table[row] not in my_list:
                my_list.append(table[row][1])

    return my_list
