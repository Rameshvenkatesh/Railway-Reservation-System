trains = {("Nizamabad","Hyderabad"):["Rayalaseema Express","Ajanta Express"],
          ("Vijayawada","Guntur"):["Palnadu express","Godavari express"]}

users = {"venkat":123, "sai":145}

user = input("enter the user name:")
password = int(input("enter the password:"))

if user in users and users[user] == password:
    print("valid user")
else:
    print("invalid user")

import random

while True:

    print("""
1.Passenger
2.Search trains
3.PNR generate
4.exit
""")

    option = int(input("enter your option:"))

    if option == 1:
        mobile = int(input("enter your mobile number:"))
        age = int(input("enter your age:"))
        gender = input("enter your gender:")
        print("Passenger registered successfully")

    elif option == 2:
        source = input("enter your source:") 
        destination = input("enter your destination:") 

        if (source, destination) in trains:      
            print("Available Trains:")

            train_list = trains[(source, destination)]

            for i in range(len(train_list)):
                print(i+1, train_list[i])

            choice = int(input("Enter train number: "))
            selected_train = train_list[choice - 1]

            print("You selected:", selected_train)

        else:
            print("No Trains available")

    elif option == 3:
        if 'selected_train' not in globals():
            print("Please search and select a train first (Option 2)")
        else:
            PNR = random.randint(55555,66666)
            print("Your PNR number is:", PNR)

            print("Ticket Booked Successfully")
            print("Passenger:", user)
            print("Train:", selected_train)
            print("Route:", source, "→", destination)
            print("PNR:", PNR)

    elif option == 4:
        print("Thank you for using Railway Reservation System")
        break