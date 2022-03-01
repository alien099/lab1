import string

name = "Аля"
age = 22
print("Можете называть меня", name, "и мне", age, "года.")

print(name*5)

user_name = input("Как вас зовут?")
user_age = input("Сколько вам лет?")
print("Ну здравствуй,", user_name, ". Ты уже такооой старый, тебе аж", user_age, "уже!")

user_age_int = int(user_age)
if user_age_int < 20:
    print("Вот тебе шутка: Сдаётся ав аренду мальчик на побегушках. Пробег 250 км.")
else:
    print("Вот тебе шутка: Кризис среднего возраста - это когда дети выросли, а ты нет.")

print(user_name[::-1])
print(user_name[::-2])
print(user_name[::2])
print(user_name[1::2])
print(user_name[1:-1])
print(user_name[-3:])
print(user_name[:5])
print(user_name[:-2])
print(user_name[2])
print(user_name[-2])

print("Длина имени:", len(user_name))
n = int(len(user_age))
if n == 2:
    print(int(user_age[0]) + int(user_age[1]))
    print(int(user_age[0]) * int(user_age[1]))
elif n == 3:
    print(int(user_age[0]) + int(user_age[1]) + int(user_age[2]))
    print(int(user_age[0]) * int(user_age[1]) * int(user_age[2]))
else:
    print(int(user_age))
    print(int(user_age))

print(user_name.upper())
print(user_name.lower())
print(user_name.capitalize())
print(user_name.swapcase())

if user_age_int < 0 or user_age_int > 150:
    print("Ошибка! Возраст должен быть указан в диапазоне от 0 до 150")
if user_name.isalpha() is False:
    print("Ошибка! Неправильно введено имя.")


c = int(input("Сколько будет 2+2*2?"))
if c == 6:
    print("Умничка! Все верно!")
else:
    print("Тебе стоит больше времени уделять математике. К сожалению, ответ неверный.")
