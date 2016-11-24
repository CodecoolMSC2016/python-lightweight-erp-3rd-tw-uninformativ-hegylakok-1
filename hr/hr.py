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
            id_ = ui.get_inputs(["Please enter an id to remove: "], "")
            remove(table, id_)
            data_manager.write_table_to_file("hr/persons.csv", table)
        elif option == "4":
            id_ = ui.get_inputs(["Please enter an id to update: "], "")
            update(table, id_)
            data_manager.write_table_to_file("hr/persons.csv", table)
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

    id = common.generate_random(table)
    list_labels = ["name", "birth_date"]
    title = "Add item to list"
    inputs = []
    inputs = ui.get_inputs(list_labels, title)
    inputs.insert(0, id)
    table.append(inputs)
    data_manager.write_table_to_file("hr/persons.csv", table)

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

    list_labels = ["name", "birthdate"]
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

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    min_year = 2016
    oldest_persons = []
    for row in table:
        born_year = row[2]
        if int(born_year) < min_year:
            min_year = int(born_year)
    for row in range(len(table)):
        if int(born_year) == min_year:
            oldest_persons.append(table[row][1])

    return oldest_persons


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    checker = 0
    sum_of_ages = 0
    current_year = 2016
    for row in table:
        born_year = int(row[2])
        sum_of_ages += current_year - born_year
        checker += 1
    average_age = sum_of_ages / checker
    min_age = 100
    list_of_names = []
    for row in table:
        born_year = int(row[2])
        result = (current_year - born_year) - average_age
        if result < 0:
            result *= -1
        if result < min_age:
            min_age = result
    for row in table:
        born_year = int(row[2])
        name = row[1]
        result = (current_year - born_year) - average_age
        if result < 0:
            result *= -1
        if result == min_age:
            if row not in list_of_names:
                list_of_names.append(name)

    return list_of_names
