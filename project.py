#1. Regular expression is a sequence of characters that forms a search pattern, basically checks if a string has a specific pattern.
import re  # Import the regex library
def validate_password(password): # Function to check if a password is strong
    # Simple regex pattern: At least 8 characters long
    pattern = r'.{8,}'  # Match any string with 8 or more characters
    if re.match(pattern, password): # Checking if the password matches the pattern
        return True
    else:
        return False
# Test the function with one password
print(validate_password("ErenJager01"))  # Should print True (valid password)



#2. Testing- seeing if your code works
def test_password_validator(): # Function to test the password validator
    print(validate_password("Password1"))  # Expected: True (valid password)
    print(validate_password("L0L12"))      # Expected: False (too short)
# Run the tests
test_password_validator()

#3. libraries- these are pre-written codes that help you save time so instead of writing a code from scartch you can just import a library that has the function you need.
#the library is another file (stringConverter.py)
import stringConverter   # Import the library
user_input = input("Enter something!!: ") # Get user input for a string
# Use the functions from the library
print(f"Length of the string: {stringConverter.string_length(user_input)}")
print(f"Uppercase version of the string: {stringConverter.to_uppercase(user_input)}" )


#4. File I/O - This basically allows you to write data to files and read data from files.
# Step 1: Ask for User Input and Write to File
file = open("favorite_color.txt", "w") # Open a file to write the favorite color. the "w" means write mode which opens the file for writing
favorite_color = input("What is your favorite color? ") # Ask the user for their favorite color
file.write(favorite_color) # Write the color to the file
file.close()  # Close the file after writing

# Step 2: Read the File and Display their Favorite Color
file = open("favorite_color.txt", "r") # Open the file to read the favorite color. the "r" means read mode which opens the file for reading only
color = file.read() # Read the content from the file
print(f"Your favorite color is: {color}") # Display their favorite color
file.close()  # Close the file after reading



#5. OOP- this is when the code is organised in to objects. a class is like a blueprint for objects while inheritance is when a class can inherit properties from another class.
class Person: # Define the class
    # initialize the person's name and age
    def __init__(self, name, age): #this function is used to assign properties to objects
        self.name = name  # Data to store the person's name
        self.age = age    # Data to store the person's age

     # Method to greet and introduce the person
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

name = input("Enter your name: ")  # Asking the user for their name
age = int(input("Enter your age: "))  # Asking the user for their age and converting it to an integer
person = Person(name, age) # Create an object of the Person class using the user's input
person.greet() # Call the greet method on the person object to display their introduction


#6 FORTUNE TELLER!!!!
#The fortunes are on (fortunes.txt)
import random  # Import the random to pick a random fortune
class FortuneTeller: # Define a class to manage the fortune-telling 
    def __init__(self, filename):
        self.filename = filename  # Store the filename where fortunes are kept

    def get_fortunes(self):
        with open(self.filename, "r") as file:  # Open the file in read mode
            return file.readlines()

    # Method to pick a random fortune
    def tell_fortune(self):
        fortunes = self.get_fortunes()  # Get the list of fortunes
        # Return a random fortune, or a message if the list is empty
        return random.choice(fortunes) if fortunes else "No fortunes available!"

# Main program
fortune_teller = FortuneTeller("fortunes.txt")  # Create an object of FortuneTeller

print("Heyy! Ask for your fortune.")

# Infinite loop to keep asking the user for a fortune
while True:
    ask = input("Do you want a fortune? (yes/no): ").lower()
    
    if ask == "yes":
        print("Your fortune:", fortune_teller.tell_fortune())  
    elif ask == "no":
        print(" oh next time :( bye!")  
        break  # Exit the loop 
    else:
        print("Please type 'yes' or 'no'.")  # Handle invalid inputs
