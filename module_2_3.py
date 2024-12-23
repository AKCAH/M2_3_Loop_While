# # M2.3 Стиль кода II. Цикл While
# Нули ничто, отрицательное недопустимо!
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
k = 0 # переменная - идентификатор
while k < len(my_list):
    if my_list[k] < 0:
        break
    elif my_list[k] == 0:
        k += 1
        continue
    print(my_list[k])
    k += 1