#Maru Puran
#November 3, 2023
#create a program to demonstrate our knowledge on while loops and how they can be used in regular programs

correct_pass = "abc123" #declare and initialize variable correct_pass to store the correct password in order to compare with user inputted one 
counter = 1 #set counter variable to 0 declare it, keeps track of how many times the user gets their password incorrect

print("Hello! Please login with the correct username and password below.") #prints the statement "please login with the correct username and password below" and greets the user to let them know what the program is abobut

username = input("\nPlease enter your username: ") #declares variable username and stores it with the user's input, prints message "please enter your username" on console to let them know what's happening
password = input("Please enter your password: ") #declares variable password and stores it with the user's input, prints message "please enter your password" on console to let them know what's happening --- this will be compared with correct_pass, or the password they should have entered

while password != correct_pass: #begins the while loop with the condition that it will run for as long as the user-entered password is not equal to the correct password
  print("\nError, incorrect password. Try again!") #lets the user know their password isn't correct by printing "error incorrect password try again" onto the console log -- inside the loop
  counter +=1 #adds 1 to the previous value held in counter for each time the loop runs, or every time the user gets their password incorrect -- inside the loop
  password = input("Please enter your password: ") #allows the user to try again and enter their password, the loop will run until this value == the correct_pass, until the user writes "abc123" in response -- inside the loop


print("\nLogin accepted! Welcome, " + username + "! It took you " + str(counter) + " tries to get your password right.") #this prints when the loop is finished running (outside the loop), when the user types in the correct password -- lets user know their login was accepted and welcomes them using the username they entered and alerts them of how many tries it took them to get it right based on the counter variable    ## puts it all into a print statement for the console log and user to see


