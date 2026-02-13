favour_word = "программирование"
print(favour_word)

first_name = 'Виталий'
last_name = 'Красилов'
new_account = last_name[5:]
temp_password = last_name[2:6]

def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]
print(account_generator("Виталий", "Красилов"))
new_account = account_generator("Виталий", "Красилов")

def password_generator(first_name, last_name):
    return first_name[-3:] + last_name[-3:]
print(password_generator("Виталий", "Красилов"))
temp_password = password_generator("Виталий", "Красилов")

company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
print(second_to_last)
final_word = company_motto[-4:]
print(final_word)

first_name = 'Боб'
last_name = 'Дейли'
first_name = 'Р' + first_name[1:]
print(first_name)

password = "theycallme\"crazy\"91"
print(password)

poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

