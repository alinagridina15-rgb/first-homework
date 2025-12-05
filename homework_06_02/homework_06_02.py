my_string = ""

while "h" not in my_string:
    my_string = input("Enter your string:")
    if "h" not in my_string:
        continue
    else:
        print("Finished")
        break


