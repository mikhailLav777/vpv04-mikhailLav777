stock = 2
minimum = 5

if stock < minimum:
    shortage = minimum - stock
    print(f"Нужно добавить мешков корма: {shortage}")
else:
    print("Запас корма в норме")