from specializaton import Specialization

def input_is_valid(msg, start=0 , end=None):
    while True:
        inp = input(msg)
        if not inp.decimal():
            print("Invalid input.Try again!")