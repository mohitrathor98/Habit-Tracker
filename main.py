from api import Pixela

while True:
    print("\n1) Create User\n2) Create Graph\n3) Post progress\n4) Update Progress\n5) Delete Progress\n6) Exit\n")
    try:
        choice = input("Your Choice: ")
    except:
        break
    
    pixela_ob = Pixela()
    if choice == 1:
        username = input("Username: ")
        print(pixela_ob.create_user(username))