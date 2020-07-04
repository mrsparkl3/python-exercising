# 04/07/20 let's start exercising.
# Today let's focus on if/else/elif statement,
# Boolean logic, and ...
# we are gonna write a simple password validator 
# Note: this won't be so secure as long as we'll store passwords in clear,
# maybe next time we could improve this code with a simple ashing function


print("Meow, today is another day for learning something new")
valid_users=["Miky", "Stefano", "Leon","Kelly"]
user= input("Enter a valid user:")
if user not in  valid_users:
  print("Your user is not valid.")
  #end program
elif user in valid_users:
  print("Access granted!")
  print("Hello, " +user+ ", how are you today?")