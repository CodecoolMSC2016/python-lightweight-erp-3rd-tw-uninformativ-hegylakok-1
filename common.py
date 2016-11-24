# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):

    generated = ''
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit = "0123456789"
    special = "$ß¤×÷"

    list_id  = []
    for n in range(2):
        list_id.append(random.choice(lowercase))
    for i in range(2):
        list_id.append(random.choice(uppercase))
    for i in range(2):
        list_id.append(random.choice(digit))
    for i in range(2):
        list_id.append(random.choice(special))
    generated = "".join(list_id)
    return generated

# Function to convert int to int and str to str in 2 dimension
