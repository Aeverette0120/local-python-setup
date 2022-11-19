def hello(first_name):
    print(f"Greetings {first_name} how are you?")

# Pass all the arguments in an ordered list

def pack(firstname, middlename,lastname):
    return[firstname,middlename,lastname]

#Use else/if statements
def eat_lunch(my_first):
    if len(my_first) == 0:
            print(f"My lunch box is empty!")
    else:
            for i in range(len(my_first)):
                if i == 0:
                    print(f"First I eat {my_first[0]}")
            else:
                print(f"Next I eat {my_first[i]}")



# Calling all of the functions

hello("Aaron")
print(pack("Mark", "Anthony", "Edwards"))
eat_lunch([])
eat_lunch(["PB&J"])
eat_lunch(["chips","applesauce","brownies"])