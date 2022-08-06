#Программа графически изображает созвездие Орион
import turtle
turtle.showturtle()

#Задать размер окна
turtle.setup(500,600)

#Задать значение звезды левого плеча
Left_shoulder = -70,200
#Задать значение звезды правого плеча
Right_shoulder = 80,180
#Задать значение левой звезды в ремня
Left_bellstar = -40,-20
#Задать значение звезды посередине ремня
Middle_bellstar = 0,0
#Задать значение правой звезды в ремне
Right_bellstar = 40,20
#Задать значение звезды в левом колене
Left_knee = -90,-180
#Задать значение звезды в правом колене
Right_knee = 120,-140

#Начертить точки в плечах и подписать названия звёзд
turtle.penup()
turtle.goto(Left_shoulder)
turtle.dot(5)
turtle.write("Бетельгейзе")
turtle.goto(Right_shoulder)
turtle.dot(5)
turtle.write("Хатиса")

#Начертить точки ремня и подписать звёзды
turtle.goto(Left_bellstar)
turtle.dot(5)
turtle.write("Альнитак")
turtle.goto(Middle_bellstar)
turtle.dot(5)
turtle.write("Альнилам")
turtle.goto(Right_bellstar)
turtle.dot(5)
turtle.write("Минтака")

#Начертить точки в коленях и подписать звёзды
turtle.goto(Left_knee)
turtle.dot(5)
turtle.write("Саиф")
turtle.goto(Right_knee)
turtle.dot(5)
turtle.write("Ригель")

#Соединить правое плечо и правое колено Ориона  линиями
turtle.pendown()
turtle.goto(Right_bellstar)
turtle.goto(Right_shoulder)

#Соединить левое плечо и левое колено Ориона  линиями
turtle.penup()
turtle.goto(Left_shoulder)
turtle.pendown()
turtle.goto(Left_bellstar)
turtle.goto(Left_knee)

#Соединить пояс Ориона  линиями
turtle.penup()
turtle.goto(Left_bellstar)
turtle.pendown()
turtle.goto(Middle_bellstar)
turtle.goto(Right_bellstar)

#Скрыть курсор черепахи
turtle.hideturtle()

#Оставить окно открытым
turtle.done()