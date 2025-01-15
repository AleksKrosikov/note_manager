# Создание заголовков и списка с ними
title1 = input("Укажите заголовок заметки: ")
title2 = input("Укажите заголовок заметки: ")
title3 = input("Укажите заголовок заметки: ")

#Создаем пустой список
title_list = []

title_list.append(title1)
title_list.append(title2)
title_list.append(title3)

# Вывод значений переменных заголовки

print("Заголовки заметки:", '; '.join(title_list))



