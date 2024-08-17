import json
user_data=[]
while True:
 print("SIGNUP/SIGNIN")
 CHOOSE=int(input("signup(1) or signin(2)"))


 if CHOOSE==1:
  username=str(input("enter your username: "))
  password=input("enter your password: ")
  phone=input("enter your phone number: ")
  user_data = {"username": username, "password": password, "phone": phone}

  print("signup successful")

  with open('Info.json', 'a') as f:
    json.dump(user_data,f)


 elif CHOOSE==2:

  username=str(input("enter your username: "))
  password=input("enter your password: ")
  with open('Info.json', 'r') as f: 
    data1=json.load(f)
    print(data1)
    if username in user_data and user_data[username]['password'] == password:
        print("Welcome USER")
    else:
        print("Incorrect username or password.")
            

    
 
    

 
  

  


# import json

# FILENAME = "data.json"


# user_data = {}

# while True:
#     print("SIGNUP/SIGNIN")
#     CHOOSE = int(input("Do you want to sign up (1) or sign in (2)? "))

#     if CHOOSE == 1:
#         # Sign-up process
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         phone = input("Enter your phone number: ")

#         # Add new user data
#         user_data[username] = {"password": password, "phone": phone}

#         # Save the updated data back to the JSON file
#         with open(FILENAME, 'a') as file:
#             json.dump(user_data, file, indent=4)

#         print("Sign-up successful!")

#     elif CHOOSE == 2:
#         # Sign-in process
#         username1 = input("Enter your username: ")
#         password1 = input("Enter your password: ")

#         # Load user data from the file to check credentials
        
#         with open(FILENAME, 'r') as file:1
#         user_data = json.load(file)

#         # Verify user credentials
#         if username1 in user_data and user_data[username1]["password"] == password1:
#           print("Welcome user")
#         else:
#             print("Incorrect username or password. Terminating the program.")
#             break  # Exit the loop and terminate the program



  

 