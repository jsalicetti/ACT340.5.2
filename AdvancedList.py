# q1

clothing= ['socks', 'pants', 'shirt', 'polo']
clothing2 = clothing.copy()
clothing2.append("skirt")

print(clothing)
print(clothing2)

# q2

clothing.insert(2,['suit jacket', 'suit pants', 'tie', 'button down'])
print(clothing)

# q3

nums= [2, 150, 14, 36, 78, 81, 14, 1000, 54, 14, 14]
print(nums.count(14))

# q4 

print(sum(nums))

# q5

print(nums[::-1])

# q6

one_to_five= [1, 2, 3, 4, 5]
print(one_to_five[-2:])

# q7

animals= ["koala", "cat", "fox", "panda", "chipmunk", "sloth"]

for item in animals:
    print(item)

# q8

# Use the list below
# Create a function that accepts a list as an argument
# Check if the data type at each index is a list
# If it is a list, check the length of the list. If it is greater than 3, add the second element to a new list.
# Return the new list


random_things= ['hello', ['breakfast', 'you', 'pencil', 2], 22, ['burrito', 'taco'],
                [22, 'win', 33, [5], 'laptop']]



def sortList(random_things):

    newList = []

    for i in random_things:

        if(type(i) is list):
           if (len(i) > 3):
            newList.append(i[2])

    print(newList)
    return newList

sortList(random_things)

#  q9

names= ['Dre', 'Seuss', 'Who', 'McCoy']
Doctors = []
for name in names:
  Doctors.append("Dr."+name)
print(Doctors)

# q10

num2= [10, 99, 85, 76, 43, 2, 77, 100, 13, 12, 42, 99, -1, -100]
i = 0
for num in num2:
    index = i + 1 
    if(num == 100):
        print(f"This 100 is at index number:{index}")

# q11

list1= ["McDonald's", "Wendy's", "", "Burger King", "", "Taco Bell"]
new_list = []
for i in list1:
  if i:
    new_list.append(i)
print(new_list)
list1= ["McDonald's", "Wendy's", "", "Burger King", "", "Taco Bell"]
new_list = []
for i in list1:
  if i:
    new_list.append(i)
print(new_list)

my_list = [1, 2, 3]
another_list = [4, 5, 6]
my_list.append(another_list)
print(my_list)  # Output: [1, 2, 3, [4, 5, 6]]

my_list = [1, 2, 3]
another_list = [4, 5, 6]
my_list.extend(another_list)
  # Output: [1, 2, 3, 4, 5, 6]
another_list.append(7)
print(my_list,another_list)