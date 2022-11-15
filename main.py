from mod import delete_data as delete
from mod import data_replacement as replace
from mod import add_new_people as add
import telebot
from bot_token import bot
from telebot import types
from logger import load

id = None
get_replacement = []

@bot.message_handler(commands=['start'])
def go_menu(message):
    username = message.from_user.username
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3=types.KeyboardButton("Открыть всю базу")
    item4=types.KeyboardButton("Удалить данные")
    item5=types.KeyboardButton("Внести изменения")
    item6=types.KeyboardButton("Добавить сотрудника")
    item7=types.KeyboardButton("Найти сотрудника")
    markup.add(item3, item4, item5, item6, item7)
    bot.send_message(message.chat.id, f"{username}, выберите режим работы", reply_markup=markup)

@bot.message_handler(commands=['id'])
def id_del(message):
    n1 = message.text.split()[1:]
    id_delete = ' '.join(n1)
    delete(id_delete)
    bot.send_message(message.chat.id,'Сотрудник удален')
    bot.send_message(message.chat.id,'Для выхода в меню используйте команду /start')

@bot.message_handler(commands=['id2'])
def id_replace(message):
    global get_replacement
    n2 = message.text.split()[1:]
    get_replacement.append(' '.join(n2))
    bot.send_message(message.chat.id,'Какой столбец меняем? Напишите в 1 строку с командой /change. Например, /change Имя')

@bot.message_handler(commands=['change'])
def column_replace(message):
    global get_replacement
    n3 = message.text.split()[1:]
    get_replacement.append(' '.join(n3))
    bot.send_message(message.chat.id,'Напишите новые данные в 1 строку с командой /new. Например, /new Иван')

@bot.message_handler(commands=['new'])
def new_data(message):
    global get_replacement
    n4 = message.text.split()[1:]
    get_replacement.append(' '.join(n4))
    replace(get_replacement)
    bot.send_message(message.chat.id,'Изменения успешно сохранены')
    bot.send_message(message.chat.id,'Для выхода в меню используйте команду /start')

@bot.message_handler(commands=['search'])
def new_data(message):
    n4 = message.text.split()[1:]
    info = ' '.join(n4)
    data = load()
    for el in data:
        for k in el.keys():
            if el.get(k) == info:
                for key,value in el.items(): 
                    bot.send_message(message.chat.id, "{:<15} {:<15}".format(key, value))
    bot.send_message(message.chat.id,'Для выхода в меню используйте команду /start')

@bot.message_handler(commands=['addnew'])
def add_people(message):
    add_data = message.text.split()[1:]
    man = {}
    man = \
        {
            'id' : add_data[0],
            'Фамилия' : add_data[1],
            'Имя' : add_data[2],
            'Отчество' : add_data[3],
            'Телефон' : add_data[4],
            'Дата рождения' : add_data[5],
            'Адрес': add_data[6],
            'Паспорт' : add_data[7]
        }
    add(man)
    bot.send_message(message.chat.id,'Cотрудник добавлен')
    bot.send_message(message.chat.id,'Для выхода в меню используйте команду /start')

@bot.message_handler(content_types='text')
def message_reply(message):
    global id
    id = message.chat.id
    a = telebot.types.ReplyKeyboardRemove()
    if 'Открыть всю базу' in message.text:
        load_data()
        bot.send_message(message.chat.id,'Начать заново /start', reply_markup=a)
    elif 'Удалить данные' in message.text:
        bot.send_message(message.chat.id,'Введите id человека, которого нужно удалить, через команду /id. Например /id 2', reply_markup=a)
    elif 'Внести изменения' in message.text:
        bot.send_message(message.chat.id,'Введите id сотрудника: /id2. Например /id2 4', reply_markup=a)
    elif 'Добавить сотрудника' in message.text:
        bot.send_message(message.chat.id,'Введите в 1 строку с командой /addnew через пробел id, фамилию, имя, отчество, телефон, дату рождения, адрес, паспорт', reply_markup=a)    
    elif 'Найти сотрудника' in message.text:
        bot.send_message(message.chat.id,'Введите любую информацию о сотруднике в 1 строку с командой /search. Например, /search Иван', reply_markup=a)    

def load_data():
    data = load()
    for el in data:
        val = [v for v in el.values()]
        val[1] = val[1] + ' ' + val[2] + ' ' + val[3]
        val.pop(3)
        val.pop(2)
        bot.send_message(id, f'id = {val[0]}, ФИО = {val[1]}, Телефон = {val[2]}, Дата рождения = {val[3]}, Адрес = {val[4]}, Паспорт = {val[5]}')
  
bot.polling()