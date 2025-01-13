# Определяем переменные

# Имя пользователя
username = "Петя Иванов"

# Заголовок заметки
title = "Покупка ЗЧ"

# Описание заметки
content = "Купить колеса"

# Статус заметки
status = "Активна"

# Дата создания заметки
created_date = "01/01/2025"

# Дата истечения заметки
issue_date = "09/01/2025"

# Упрощенное представление дат
temp_created_date = created_date[0:2] + "." + created_date[3:5]
temp_issue_date = issue_date[0:2] + "." + issue_date[3:5]

# Вывод значений переменных
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки:", temp_issue_date)

