#Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
#You will then be given an unknown number of names to query your phone book for.
#For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
#if an entry for  is not found, print Not found instead.

number_book={}
#for how many friends to add, add to dictionary
for x in range(int(input())):
    user_input = input()
    key, value = user_input.split(" ")
    number_book[key] = value
#for undetermined amount of names, see if inputed name is in dictionary. Else print not found 

while (True):
    try:
        name = str(input())
            #if name is there print Name=num
        if name not in number_book:
            print("Not Found")
        else:
            print(name + "=" + number_book[name])
    except:
        break
