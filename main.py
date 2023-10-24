print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы:")
# Question="Как называется компания , которая создается для развития новой идей и инновацоного продукта?"
# Answer="Стартап"
# print(Question)
# user_input = input("Введите свой ответ: ")
# if user_input.lower() == Answer.lower():
#   print("Правильно")
# else:
#   print("Неправильно")
questions = [
  "1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?", 
  "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
  "3. Как называется капитал, который дают инвесторы на развитие стартапа?", 
  "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?", 
  "5. Какой план создают перед тем, как открывать стартап и занимать деньги?", 
  "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?", 
  "7. Как называется разница между выручкой и затратами компании?"
]

answers = [
  "Стартап",
  "Инвестор",
  "Инвестиция", 
  "MVP", 
  "Бизнес-план", 
  "Конкуренты",
  "Прибыль"
]
score = 0


print(questions[0])
user_input = input("Введите свой ответ: ")
if user_input.lower() == answers[0].lower():
  print("Правильно")
  score = score + 1
else:
  print("Неправильно")
print(questions[1])
user_input = input("Введите свой ответ: ")
if user_input.lower() == answers[1].lower():
  print("Правильно")
  score = score + 1
else:
  print("Неправильно")
print(questions[2])
user_input = input("Введите свой ответ: ")
if user_input.lower() == answers[2].lower():
  print("Правильно")
  score = score + 1
else:
  print("Неправильно")
print(questions[3])
user_input = input("Введите свой ответ: ")
if user_input.lower() == answers[3].lower():
  print("Правильно")
  score = score + 1
else:
  print("Неправильно")
print(questions[4])
user_input = input("Введите свой ответ: ")
if user_input.lower() == answers[4].lower():
  print("Правильно")
  score = score + 1
else:
  print("Неправильно")
print(questions[5])
user_input = input("Введите свой ответ: ")
if user_input.lower() == answers[5].lower():
  print("Правильно")
  score = score + 1
else:
  print("Неправильно")
print(questions[6])
user_input = input("Введите свой ответ: ")
if user_input.lower() == answers[6].lower():
  print("Правильно")
  score = score + 1
else:
  print("Неправильно")
if score > 5:
  print("Это отличный результат! Ты много знаешь о стартапах.")
elif score > 3:
  print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о стартапах.")
else:
  print("Видимо, ты только начинаешь свой путь к стартапам! Ты ещё много чего узнаешь о мире, где мы живём.")
# name = input('Твое имя: ')
# #сity = input('Твое город: ')
# print("Ваше имя",  name)
# #print(city)
# product = input("Введите продукт:  ")
# money = int(input("Введите цену продукта: "))
# print("Сегодня скидки!")
# print("Вы купили ", product, "за", money - 10,"рублей")
# car = input("Введите машину:  ")
# money = int(input("Введите цену машины: "))
# print("Сегодня скидки!")
# print("Вы купили ", car, "за", money - 100000,"рублей")
# x = "привет"
# print(type(x))
# x = int(float(input()))
# print (x)
# message = "Hello"
# name = "Nurali"
# print(message + " " + name)
# a = "12"
# b = "5"
# c = a + b
# print(c)
# projects = ["Сайт для отеля", "Игра-стрелялка", "Калькулятор", "Видеохостинг"]
# print(projects[2])
