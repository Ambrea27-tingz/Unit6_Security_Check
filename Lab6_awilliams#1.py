"""Name: Ambrea Williams
   
   Date: 06/13/2025

   Unit 6: Lab 6 - Security Password Checker

   Description: login program that checks a username and password from a dictionary, 
   assigns a security level, and greets the user upon successful login. 
   Guests can log in with limited access using “guest”/“guest”
   """

"""#S1: Create a dictionary of usernames and passwords"""

user_files = {
    "Sally": "PrettyInPink@614",
    "Paul": "TomandJerry@123",
    "Sabrina": "SabrinaTheTeenageWitch@456",
    "guest": "guest",
    }

"""#S2: Shows users their security levels"""

security_levels = {
    "Sally": 1,
    "Paul": 2,
    "Sabrina": 2,
    "guest": 3
}

"""Allows a maximum of 3 login attempts."""
attempts = 3
while attempts > 0:

    """#S3: Ask the user for their username"""

    username = input("Enter your username: ")
    
    """#S4: Check if the username exists"""
    if username not in user_files:
        print("Invalid username. Please try again.")
        attempts -= 1
        continue # Restart the loop

    """#S5: Ask for the password (atp the username exists)"""
    password = input("Enter the details of your password: ")

    """#S6: Validate the password"""

    if password == user_files[username]:
        
      """#S7: Assign and display security level"""
      level = security_levels[username]
      print(f"Welcome, {username}! Your security level is {level}.")
      break  # Exit loop with a successful login
    else:
        print("Incorrect password. Please try again.")
        attempts -= 1

"""#S8: Assign and display security level"""

if attempts == 0:  # If attempts run out, deny access
    print("Too many failed attempts. Access denied.")







