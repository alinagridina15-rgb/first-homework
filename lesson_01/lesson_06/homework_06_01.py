my_string= input("Validation code error:")
my_set = set(my_string)

if len(my_set)>10:
    print(True)
else:
    print(False)

