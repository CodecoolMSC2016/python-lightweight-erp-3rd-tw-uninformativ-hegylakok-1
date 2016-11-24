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

    # you code

    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    # your code

    pass


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
