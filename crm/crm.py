# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
    table = data_manager.get_table_from_file("crm/customers.csv")

    while True:
        options = ["Print the default table of records",
                "Add an item to the table",
                "Remove from table",
                "Update an item in the table",
                "What is the id of the customer with the longest name?",
                "Which customers has subscribed to the newsletter?"]

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
            get_longest_name_id(table)
        elif option == "6":
            get_subscribed_emails(table)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        return


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    title_list = ["id", "name", "email", "subscribed"]
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


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):

    max = 0
    my_list = []
    for row in range(len(table)):
        if len(table[row][1]) > max:
            max = len(table[row][1])
    for row in range(len(table)):
        if len(table[row][1]) == max:
            my_list.append(table[row])
        n = len(my_list)
        while n > 1:
            n -= 1
            for row in range(len(my_list) - 1):
                if my_list[row][1].lower() > my_list[row + 1][1].lower():
                    my_list[row], my_list[row + 1] = my_list[row + 1], my_list[row]
    return my_list[0][0]


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")


def get_subscribed_emails(table):

    my_list = []
    for row in range(len(table)):
        if table[row][3] == "1":
            string = "%s;%s" % (table[row][2], table[row][1])
            my_list.append(string)
    return my_list
