#WAP tocount the number of upper case and lower case letters in it.

User_input = input("Enter your Word :")
upper_count = 0
lower_count = 0
for i in User_input:
    if(i.islower()):
        lower_count= lower_count +1
    elif(i.isupper()):
        upper_count= upper_count +1
print("Count of Lowercase Digits :",lower_count)
print("Count of Uppercase Digits :",upper_count) 
        
