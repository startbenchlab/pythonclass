from myFun import *

# Myprint()
# Add(10, 20)
# Floor(9, 1)

# def describe_pet(animal_type, pet_name):
#     print(f"I have a {animal_type} named {pet_name}.")

# def describe_pet(pet_name, animal_type):
#     print("I have a " + animal_type + " named " + pet_name + ".")
    
def calculate_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(calculate_sum(10, 20, 30,20)) # Result: 60

def calculate_product(*numbers):

    for n in numbers:
        print(n)
        
        
        
print(calculate_product(10, 20, 30,20))

multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12


def multiply(x, y):
    return x * y

print(multiply(3, 4))  # Output: 12