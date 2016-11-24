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

        ui.print_menu("Customer Relationship Management", options, "Back")
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
            data_manager.write_table_to_file("crm/customers.csv", table)
        elif option == "4":
            id_ = ui.get_inputs(["Please enter an id to update: "], "")
            update(table, id_)
            data_manager.write_table_to_file("crm/customers.csv", table)
        elif option == "5":
            label = "The id of the customer is:"
            result = get_longest_name_id(table)
            ui.print_result(result, label)
        elif option == "6":
            label = "Newsletter subscribers:"
            result = get_subscribed_emails(table)
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

    title_list = ["id", "name", "email", "subscribed"]
    ui.print_table(table, title_list)
    start_module()


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    id = common.generate_random(table)
    list_labels = ["name", "email", "subscribed"]
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

    list_labels = ["name", "email", "subscribed"]
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


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):

    longest_name = 0
    sorted_list = []
    for row in table:
        name = row[1]
        if len(name) > longest_name:
            longest_name = len(name)
    for row in table:
        name = row[1]
        if len(name) == longest_name:
            sorted_list.append(row)
        lenght_of_list = len(sorted_list)
        while lenght_of_list > 1:
            lenght_of_list -= 1
            for row in range(len(sorted_list) - 1):
                if sorted_list[row][1].lower() > sorted_list[row + 1][1].lower():
                    sorted_list[row], sorted_list[row + 1] = sorted_list[row + 1], sorted_list[row]
    return sorted_list[0][0]


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")


def get_subscribed_emails(table):

    subscribers = []
    for row in table:
        email = row[2]
        name = row[1]
        subscribed = row[3]
        if subscribed == "1":
            string = "%s;%s" % (email, name)
            subscribers.append(string)
    return subscribers
