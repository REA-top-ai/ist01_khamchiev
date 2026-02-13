answers = (
    1, 2, 3, 2, 1,
    2, 1, 3, 1, 2,
    1, 2, 3, 3, 2,
    1, 2, 1, 2, 1
)
user = []
for i in range(20):
    a = int(input("Введите ответ " + str(i + 1) + ": "))
    user.append(a)
if tuple(user) == answers:
    print("Экзамен сдан")
else:
    print("Экзамен провален")
