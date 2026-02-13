product = ["торт", 1]
print(product)

household_chemicals = [["стиральный порошок", 1],["средство для мытья посуды", 1]]
print(household_chemicals)

names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

orders = ['маргаритки', 'васильки']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders)

orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
broken_prices = [5, 3, 4, 5, 4, 4]
print(broken_prices)

list1 = list(range(1,9))
list2 = list(range(0,7))
print(list1)
print(list2)

list1 = list(range(5, 16, 3))
list2 = list(range(0, 40, 5))
print(list1)
print(list2)


first_names = ["Эйнсли", "Бен", "Чани", "Депак"]
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = list(range(4))

