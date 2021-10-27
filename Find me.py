from random import randint
superList=[randint(1,10) for i in range(10)]
print(superList)
a = int(input("Введите число от 1 до 10: "))
b = [index for index, value in enumerate(superList) if value == a]
print(f"Число {a} находится в списке под номером: {b}")
