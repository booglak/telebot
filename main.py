import telebot, config, privat_bank_course

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "Доступные команды: \n"
                                      "/help - описание доступных команд \n"
                                      "/course - текущий курс доллара в приват банке \n"
                                      "/add_list - добавить новый список чего-либо \n"
                                      "/get_list - посмотреть последний введенный список \n"
                                      "/clear_list - очистить список \n"
                                      "/complete_list - дополнить список \n")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, я Гошин бот. Доступные команды, можно посмотреть тут /help")


@bot.message_handler(commands=["course"])
def course(message):
    c1 = privat_bank_course.get_usd_course_sale()
    c2 = privat_bank_course.get_usd_course_buy()
    bot.send_message(message.chat.id, f"Курс продажи доллара в привате: {c1} \n"
                                      f"Курс покупки доллара в привате: {c2}")


# Команда присваивает константе из конфига True для того что бы сработала функция add
@bot.message_handler(commands=["add_list"])
def add_list(message):
    bot.send_message(message.chat.id, "Введи список!")
    config.LIST_OPEN = True


# Функция добавляет в строковую переменную введенный список, вызывается только после add_list
@bot.message_handler(func=lambda message: config.LIST_OPEN == True)
def add(message):
    config.MANUAL_LIST = message.text
    config.LIST_OPEN = False


# Команда присваивает константе из конфига True для того что бы сработала функция complete
@bot.message_handler(commands=["complete_list"])
def complete_list(message):
    bot.send_message(message.chat.id, "Дополни список список!")
    config.LIST_COMPLETE = True


# Функция добавляет в заполненную строку новые значения, вызывается только после complete_list
@bot.message_handler(func=lambda message: config.LIST_COMPLETE == True)
def add(message):
    config.MANUAL_LIST += ('\n' + message.text)
    config.LIST_COMPLETE = False


@bot.message_handler(commands=["clear_list"])
def clear_list(message):
    bot.send_message(message.chat.id, "Список очищен")
    config.MANUAL_LIST = ''
    config.LIST_OPEN = False


@bot.message_handler(commands=["get_list"])
def get_list(message):
    bot.send_message(message.chat.id, "Последний введенный список:")
    bot.send_message(message.chat.id, config.MANUAL_LIST)


if __name__ == "__main__":
    bot.polling(none_stop=True)
