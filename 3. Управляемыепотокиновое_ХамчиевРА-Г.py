print((6 * 6) - 1 == 8 + 1 )
print(13 - 7 != (3 * 2) + 1 )
print(3 * (2 - 1) == 4 - 1 )
print((6 * 6) - 1 >= 8 + 1)
print(13 - 7 <= (3 * 2) + 1 )
print(3 * (2 - 1) > 4 - 1 )

#bool_variable = true
#True и False должны писаться с большой буквы, а так он не воспринимает ее не как число или же строка ни bool
bool_variable = 'true'
print(type(bool_variable))
#тип строка. не логическая переменная потому что ей не присвоен какой-либо логич. оператор bool
bool_variable2 = True
print(type(bool_variable2))

user_name = 'Ангелина'
Dmitriy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'
welcome = 'Добро пожаловать!'
if user_name == 'Дмитрий':
    print(Dmitriy_check)
if user_name == 'Ангелина':
    print(welcome)
user_name = 'Дмитрий'
if user_name == 'Дмитрий':
    print(Dmitriy_check)
if user_name == 'Ангелина':
    print(welcome)

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
user_name = input("Введите ваше имя: ")
ARM = int(input("Введите номер АРМ: "))
if ARM == 1 and user_name == "Дмитрий":
    print("Добро пожаловать!")
elif ARM == 2 and user_name == "Ангелина":
    print("Добро пожаловать!")
elif ARM == 3 and user_name == "Василий":
    print("Добро пожаловать!")
elif ARM == 4 and user_name == "Екатерина":
    print("Добро пожаловать!")
elif user_name != "Дмитрий":
    print("Логин или пароль не верный, попробуйте еще раз")
else:
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
print(statement_one)
print(statement_two)

user_name = input("Введите ваше имя: ")
ARM = int(input("Введите номер АРМ: "))
if (ARM == 1 and user_name == "Дмитрий") or (ARM == 2 and user_name == "Ангелина") or (ARM == 3 and user_name == "Василий") or (ARM == 4 and user_name == "Екатерина"):
    print("Добро пожаловать!")
else:
    if user_name != "Дмитрий":
        print("Логин или пароль не верный, попробуйте еще раз")
    else:
        print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")

grade = float(input())
if grade >= 4.0:
    print("A")
elif grade >= 3.0:
    print("B")
elif grade >= 2.0:
    print("C")
elif grade >= 1.0:
    print("D")
else:
    print("F")


