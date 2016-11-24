

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):

    # címsor oszlopainak szélessége
    len_title = []
    for item in title_list:
        len_title.append(len(item))
    # az oszlopszélességek meghatározása
    max_lenght_in_table = [max(len(str(item)) for item in line) for line in zip(*table)]
    i = 0
    for i in range(0, len(max_lenght_in_table)):
        if max_lenght_in_table[i] < len_title[i]:
            max_lenght_in_table[i] = len_title[i]
    # tábla szélességének meghatározása
    table_lenght = 0
    for item in max_lenght_in_table:
        table_lenght += int(item)
    table_lenght = table_lenght + int(len(title_list))*2
    # tábla rajzolása
    print("/", "-"*table_lenght, chr(92))
    for index in range(0, len(title_list)):
        print("|" + title_list[index].center(max_lenght_in_table[index]+2), end = "")
    print("|")
    for line in table:
        for index in range(0, len(title_list)):
            print("|" +  "-"*(max_lenght_in_table[index]+2), end = "")
        print("|")
        for index in range(0, len(title_list)):
            print("|" + line[index].center(max_lenght_in_table[index]+2), end = "")
        print("|")
    print(chr(92), "-"*table_lenght, "/")
    print("\n")


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

   print()
   print(label, "\n")
   if type(result) == list:
       for row in result:
           print(row, "\n")
       print()
   elif type(result) == dict:
       for key, value in result.items():
           print(key, ":", value)
       print()

   else:
       print(result, "\n")



# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):

    print("\n" + title + "\n")
    counter = 0
    for i in list_options: 
        counter += 1
        print("(" + str(counter) + ") " + i)
    print("(0) " + exit_message)
    


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    
    inputs = []
    print(title)
    for label in list_labels:
        label = label + " : "
        usr_in = input(label)
        inputs.append(usr_in)

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    # your code

    pass
