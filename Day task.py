# Программа показывает день недели, в зависимости от введённых цифр
count = int(input("Введите любое число от 1 до 7, чтобы узнать день недели: "))

def input_validation ():
    global count
    while count < 1 or count > 7:
        print("Вы ввели недопустимое значение.Пожалуйста введите любое число от 1 до 7")
        count = int(input("Введите любое число от 1 до 7, чтобы узнать день недели:"))

def process():
    print("Хотите узнать ещё день? Тогда введите да в следующем окне")
    continue_task = input("Продолжить?: ")
    while continue_task == "да":
        count = int(input("Введите любое число от 1 до 7, чтобы узнать день недели: "))
        input_validation()
        determination_day()
        process()
    else:
        print("Спасибо! Удачного дня!")

def determination_day ():
    global count
    if count == 1:
        print("Сегодня понедельник")
    elif count == 2:
        print("Сегодня вторник")
    elif count == 3:
        print("Сегодня среда")
    elif count == 4:
        print("Сегодня четверг")
    elif count == 5:
        print("Сегодня пятница")
    elif count == 6:
        print("Сегодня суббота")
    else:
        print("Сегодня воскресенье")
    process()


input_validation()
determination_day()
