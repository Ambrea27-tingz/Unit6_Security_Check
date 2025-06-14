"""Name: Ambrea Williams
   
   Date: 06/07/2025

   Unit 6: Lab 6 - Security Password Checker

   Description: login program that checks a username and password from a dictionary, 
   assigns a security level, and greets the user upon successful login. 
   Guests can log in with limited access using “guest”/“guest”
   """

# Step 1: Create a dictionary of usernames and passwords
user_files = {
    "Sally": {
        "password": "PrettyInPink@614"
    },

    "Paul": {
        "password": "TomandJerry@123"
    },

    "Sabrina": {
        "password": "SabrinaTheTeenageWitch@456"
    },
    
    "guest": {
        "password": "guest"
    },
}

#2: Defines security levels
security_levels = {
    "Sally": 1,
    "Paul": 2,
    "Sabrina": 2,
    "guest": 3
}

"""Allows a maximum of 3 login attempts."""
attempts = 3
while attempts > 0:

#3: Ask the user for their username
    username = input("Enter your username: ")
    
    # Step 4: Check if the username exists
    if username not in user_files:
        print("Invalid username. Please try again.")
        attempts -= 1
        continue # Restart the loop




#5: Ask for the password (since username exists)







#6: Validate the password





#7: Assign and display security level








