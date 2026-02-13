def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
def c_to_f(c_temp):
    f_temp = c_temp * 9 / 5 + 32
    return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


def get_force(train_mass,train_acceleration):
    return train_acceleration * train_acceleration

def get_energy(bomb_mass, c = 3 * 10 ** 8):
    return bomb_mass * c ** 2

def get_work(mass,yskr,distant):
    return get_force(mass,yskr) * distant
train_mass = 22680
train_acceleration = 10
train_distance = 100
train_force = get_force(train_mass,train_acceleration)
print(train_force)
print("Поезд GE поставляет",train_force," ньютонов")
bomb_energy = get_energy(1)
print("1 кг бомбы составляет",bomb_energy," Джоулей")
train_work = get_work(train_mass,train_acceleration,train_distance)
print("Поезд выполняет",train_work," Джоулей за",train_distance," метров.")


clothes = "дом одежда"
def shmot(day_time):
    print("у меня большой гардероб")
    print(day_time + " лучше подходит " + clothes)
shmot("Ночью")

meal = "дом"

def eda(eat_time):
    print("мои предпочтения в еде")
    print(eat_time + " лучше подходит " + meal)
eda("ужин")


def done(user_name, ARM):
    if user_name== 'Дмитрий' and ARM == 1:
        return True
    if user_name== 'Ангелина' and ARM == 2:
        return True
    if user_name == 'Василий' and ARM == 3:
        return True
    if user_name == 'Екатерина' and ARM == 4:
        return True
    return False
user_name = input('Введите своё имя\n')
ARM = int(input('Введите свой APM'))
text_for_users = 'Добро пожаловать'
Dmitiy_check ='Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'
if done(user_name, ARM):
    print(text_for_users)
elif user_name== 'Дмитрий':
    print(Dmitiy_check)
else:
    print('Логин или пароль не верный, попробуйте еще раз')

def rang(grade):
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
grade = float(input("Ведите балл"))
rang(grade)
