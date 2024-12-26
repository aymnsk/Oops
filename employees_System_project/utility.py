def input_is_valid(msg, start=0, end=None):
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print("Invalid Input. Try Again!!")

        elif start is not None and end is not None:
            if not(start<= int(inp) <=end):
                print("invalid range. Try again!!")
            else:
                return int(inp)
        else:
            return int(inp)
        