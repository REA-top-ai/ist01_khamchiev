list1 = range(2, 20, 2)
list1_len = len(list1)
print(list1_len)
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)

shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5)
print(last_element)

suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase[0:2]
print(beginning)
print(len(beginning))
beginning = suitcase[0:4]
print(beginning)
middle = suitcase[2:4]
print(middle)

suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
start = suitcase[0:3]
print(start)

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie','Jake', 'Jake', 'Jake', 'Laurie', 'Cassie','Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie','Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = 0
for name in votes:
    if name == 'Jake':
        jake_votes = jake_votes + 1
print(jake_votes)

addresses = ['221 B Baker St.','42 Wallaby Way','12 Grimmauld Place','742 Evergreen Terrace','1600 Pennsylvania Ave','10 Downing St.'   ]
print("До сортировки:")
print(addresses)
addresses.sort()
print("После сортировки:")
print(addresses)

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)

# Список товаров
inventory = ['двуспальная кровать', 'двуспальная кровать', 'изголовье','двуспальная кровать', 'двуспальная кровать', 'комод','комод', 'стол', 'стол', 'тумбочка','тумбочка', 'королевский кровать', 'двуспальная кровать','двуспальная кровать', 'две односпальные кровати','две односпальные кровати', 'простыня', 'простыня','подушка', 'подушка']
inventory_len = len(inventory)
print("Всего товаров:", inventory_len)

first = inventory[0]
print("Первый:", first)

last = inventory[-1]
print("Последний:", last)

inventory_2_6 = inventory[2:6]
print("С 2 по 6:", inventory_2_6)

first_3 = inventory[0:3]
print("Первые 3:", first_3)

twin_beds = inventory.count('две односпальные кровати')
print("Односпальных кроватей:", twin_beds)

inventory.sort()
print("После сортировки:", inventory)

