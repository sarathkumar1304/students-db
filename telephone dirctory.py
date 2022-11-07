import pymongo
#to create

def create():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client["mydbs"]
    mycol = mydb["phnumbers"]
    name1 = input("Enter name:")
    phnum = input("Enter num:")
    gender = input("Enter gender:")
    email = input("enter email.id:")
    address = input("Enter address:")
    mydict = {"name": f'{name1}',
              "phnum": f'{phnum}',
              "gender": f'{gender}',
              "email": f'{email}',
              "address": f'{address}'
             }
    mycol.insert_one(mydict)

    for i in mycol.find(mydict):
        print(i)
    print("*** Created successfully ***")

# To update
def update():
    print("Type [1] to update name\nType [2] to update number\nType [3] to update email\nType [4] to update address\nType [5] to update or add an newfeild")
    opt = int(input("Enter number:"))
    # TO update  name
    if opt == 1:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydbs"]
        mycol = mydb["phnumbers"]
        name = input("Enter old name:")
        newname = input("Enter new name to update:")
        myquery = {"name": f'{name}'}
        newvalue = {"$set": {"name": f'{newname}'}}
        y=mycol.update_one(myquery, newvalue)
        for i in mycol.find():
            print(i)

        print("Update successfully")
    # To update phone number
    if opt == 2:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydbs"]
        mycol = mydb["phnumbers"]
        name = input("Enter name of the contact:")
        new_phnum = input("Enter new phnum to update:")
        myquery = {"name": f'{name}'}
        newvalue = {"$set": {"phnum": f'{new_phnum}'}}
        mycol.update_one(myquery, newvalue)

        for x in mycol.find():
            print(x)
        print("Update successfully")
    #to upadate email id
    if opt == 3:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydbs"]
        mycol = mydb["phnumbers"]
        name = input("Enter name of the contact:")
        new_email = input("Enter new email to update:")
        myquery = {"email": f'{name}'}
        newvalue = {"$set": {"email": f'{new_email}'}}
        mycol.update_one(myquery, newvalue)
        print("Update successfully")
        for x in mycol.find():
            print(x)
    #to update address
    if opt == 4:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydbs"]
        mycol = mydb["phnumbers"]
        name= input("Enter name:")
        new_address = input("Enter new address to update:")
        myquery = {"name": f'{name}'}
        newvalue = {"$set": {"address": f'{new_address}'}}
        mycol.update_one(myquery, newvalue)
        print("Update successfully")
        for x in mycol.find():
            print(x)
    #to add a new feild to th document
    if opt==5:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydbs"]
        mycol = mydb["phnumbers"]
        name=input("Enter name to add a field")
        field_name=input("Enter feild name:")
        feild_det=input("Enter feild details")
        mycol.update_one({"$set":{f'{field_name}': f'{feild_det}'}})
        print("Updated successfully")
        for x in mycol.find():
            print(x)

# To retrive
def read():
    global mycol
    print("Type [1] to serach based on name\nType [2] to search  based on number")
    opt = int(input("Enter number:"))
    if opt == 1:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydbs"]
        mycol = mydb["phnumbers"]
        myquery = input("Enter name to search:")
        search = {"name": f'{myquery}'}


        #mydoc = mycol.find()
        for i in mycol.find((search)):
          print(i)

    if opt == 2:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydbs"]
        mycol = mydb["phnumbers"]
        myquery1 = input("Enter number to search:")
        search1 = {"phnum": f'{myquery1}'}
        mydoc = mycol.find(search1)
        for y in mydoc:
            print(y)

#To delete a document
def delete():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client["mydbs"]
    mycol = mydb["phnumbers"]
    myquery = input("Enter name to delete :")
    x=mycol.delete_one({"name": f'{myquery}'})

    print("___*** Delete successfully ***___")
    print("___*** Remaining Details ***___")
    for x in mycol.find():
        print(x)

def options():
    print("-----***** TELEPHONE DIRECTORY *****----")
    print("------------** WELCOME'S YOU **--------------")
    print("Please Enter Number")
    print("Type 1 --> to create a contact\nType 2 --> to update a contact\nType 3 --> to read a contact\nType 4 --> to delete a contact")
    option = int(input("Enter Number:"))

    if option == 1:
        create()
    if option == 2:
        update()
    if option == 3:
        read()
    if option == 4:
        delete()
options()