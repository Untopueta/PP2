def check(str):
    x = {"upper": 0, "lower": 0}

    for i in str:
        if i.isupper():
            x["upper"] += 1
        elif i.islower():
            x["lower"] += 1
        else:
            pass
    
    print("N of Upper characters: ", x["upper"])

    print("N of Lower Characters: ", x["lower"])

mystr = input("Your str: ")
check(mystr) 
