# Информация о заметке
note = []

# Имя пользователя
username = input("Назовите Ваше имя: ")
note.append(username)

# Заголовки заметки
title_list = [] # Пустой список для хранения заголовков.

title1 = input("Укажите заголовок заметки: ")
title_list.append(title1)

title2 = input("Укажите заголовок заметки: ")
title_list.append(title2)

title3 = input("Укажите заголовок заметки: ")
title_list.append(title3)

note.append(title_list)

# Описание заметки
content = input("Опишите заявку: ")
note.append(content)

# Статус заметки
status = input("Укажите статус заявки: ")
note.append(status)

# Дата создания заметки
created_date = input("Укажите дату создания заявки, например '01/01/2025': ")

# Дата истечения заметки
issue_date = input("Назначьте дедлайн, например 09/01/2025: ")

# Упрощенное представление дат
temp_created_date = created_date[0:2] + "." + created_date[3:5]
note.append(temp_created_date)

temp_issue_date = issue_date[0:2] + "." + issue_date[3:5]
note.append(temp_issue_date)

# Вывод значений переменных
print("Имя пользователя:", note[0])
print("Заголовок заметки:", "; ".join(note[1]))
print("Описание заметки:", note[2])
print("Статус заметки:", note[3])
print("Дата создания заметки:", note[4])
print("Дата истечения заметки:", note[-1])