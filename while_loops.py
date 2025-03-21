''' For loops are used when you run (execute) a block of code one time 
for each item listed in a list 

while loops are used when we want to run code until a condition is met.'''

'''current_number=1 

while current_number<=5:
    print(current_number) 
    current_number +=1'''

  '''  # User quitting a program 

prompt= "\nTell me your favorite candy,and I will say it back to you:"
prompt +="\nEnter 'quit' to end the program." #adds ands additional line 

message="" #need this to run the while loop the first time. 
while message !="quit": # != means not equal to 
    message=input(prompt)
    print(message)'''

#Using a break to exit a loop 

prompt ="\nPlease enter a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished)"

while True:
  city=input(prompt)
  break 
else:
  print(f"I"'d love to go to {city.title()!}")