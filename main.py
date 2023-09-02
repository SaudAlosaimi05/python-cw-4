def my_name():
    print("my name is Saud")

#part two 

def my_meal(food,drink):
    print(f"I like to eat {food} and while drinking {drink}")
my_meal("burger","cola")

#part three

def cube(number):
    return number**3
def by_three(number):
    if number % 3 ==0 :
        return cube(number)
    else :
         return "false"
resault = by_three(int(input("enter your number:")))
print(resault)