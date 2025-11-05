def askUser():
    bagItems = {}  # Create a variable of type dictionary named bagItem
    def addToBagItems(category: str, value: int):
        bagItems[category] = value
    loop = True
    print("Give me the items of your collection:")
    while loop:
        c = input("Item Name: ")
        if c == "":
            def addToBagItems(category: str, value: int):
                bagItems[category] = value
            loop = False
        else:
            v = int(input("How Much: "))
            if v == "":
                v = 0
            addTobagItem(category=c, value=v)



if __name__=="__main__":
    print("Hello World")