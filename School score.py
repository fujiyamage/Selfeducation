#Программа позволяет высчитать средний бал студента
#Получаем у пользователя общее количество студентов и контрольных работ
num_students = int(input("Введите, сколько у вас студентов?:"))
num_test = int(input("Введите, сколько вы хотите получить оценок?:"))

#Определение среднего балла  для каждого студента
for student in range(num_students):
    print("Номер студента", student + 1)
    print("------------")

    for test in range (num_test):
        total = 0.0  # Создаем накопитель оценки
        print("Номер контрольный работы", test + 1)
        score =float(input(": "))
        total += score
        average = total / num_test #Рассчитываем средний бал студента

    print("Средний бал студента номер", student + 1, "составляет", average)
 