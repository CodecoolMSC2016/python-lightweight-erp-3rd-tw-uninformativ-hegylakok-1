# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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

    table = data_manager.get_table_from_file("accounting/items.csv")

    while True:
        options = ["Print the default table of records",
                   "Add an item to the table",
                   "Remove from table",
                   "Update an item in the table",
                   "Which year has the highest profit?",
                   "What is the average (per item) profit in a given year?"]

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
            data_manager.write_table_to_file("accounting/items.csv", table)
        elif option == "4":
            id_ = ui.get_inputs(["Please enter an id to update: "], "")
            update(table, id_)
            data_manager.write_table_to_file("accounting/items.csv", table)
        elif option == "5":
            which_year_max(table)
        elif option == "6":
            avg_amount(table, year)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")

        return


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    title_list = ["id", "month", "day", "year", "type", "amount"]
    ui.print_table(table, title_list)
    start_module()  # Azért kell, hogy ne a Main menübe ugorjon vissza egyből, hanem itt mardjon!!


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    id = common.generate_random(table)
    list_labels = ["month", "day", "year", "type", "amount"]
    title = "Add item to list"
    inputs = []
    inputs = ui.get_inputs(list_labels, title)
    inputs.insert(0, id)
    table.append(inputs)
    data_manager.write_table_to_file("accounting/items.csv", table)

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
    list_labels = ["month", "day", "year", "type", "amount"]
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

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    results = {}
    max = 0
    max_year = 0
    for row in table:
        row_type = row[4]
        year = int(row[3])
        value = int(row[5])
        if row_type == "out":
            value *= -1
        if year in results.keys():
            results[year] += value
        else:
            results[year] = value
    for year, value in results.items():
        if value > max:
            max = value
            max_year = year
    return max_year

# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)


def avg_amount(table, year):
    given_year = year
    sum = 0
    counter = 0
    for row in table:
        row_type = row[4]
        value = int(row[5])
        year = int(row[3])
        if year == given_year:
            if row_type == "out":
                sum -= value
            else:
                sum += value
            counter += 1
    return sum / counter
