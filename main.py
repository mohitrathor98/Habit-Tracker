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
    
    elif choice == 2:
        graph_id = input("Graph Id: ")
        graph_name = input("Graph Namr: ")
        unit = input("Unit for graph(commit/kilogram/calory): ")
        data_type = input("Data type(int/float): ")
        
        print(pixela_ob.create_new_graph(graph_id, graph_name, unit, data_type))
        
    