from api import Pixela

while True:
    print("\n1) Create User\n2) Create Graph\n3) Post progress\n4) Update Progress\n5) Delete Progress\n6) Exit\n")
    try:
        choice = int(input("Your Choice: "))
    except:
        break
    
    pixela_ob = Pixela()
    if choice == 1:
        username = input("Username: ")
        print(pixela_ob.create_user(username))
    
    elif choice == 2:
        graph_id = input("Graph Id: ")
        graph_name = input("Graph Name: ")
        unit = input("Unit for graph(commit/kilogram/calory/days, etc): ")
        data_type = input("Data type(int/float): ")
        
        print(pixela_ob.create_new_graph(graph_id, graph_name, unit, data_type))
    
    elif choice == 3:
        graph_name = input("Graph Name: ")
        quantity = input("Post quantity: ")
        
        print(pixela_ob.post_progress(graph_name, quantity))
    
    elif choice == 4:
        graph_name = input("Graph Name: ")
        quantity = input("Quantity to update: ")
        
        print(pixela_ob.update_progress(graph_name, quantity))
        
    elif choice == 5:
        graph_name = input("Graph Name: ")
        
        print(pixela_ob.delete_progress(graph_name))
    
    else:
        break
        
    