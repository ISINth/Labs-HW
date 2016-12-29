from class_vk import myvk
 
#Введите id пользователя вк...
user_id = int()
user_id = input('Входные данные: ')

vk = myvk(user_id)
vk.PrintAnswer()
