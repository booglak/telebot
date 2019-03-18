import telebot, config, privat_bank_course

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "Доступные команды: \n"
                                      "/help - описание доступных команд \n"
                                      "/course - текущий курс доллара в приват банке \n"
                                      "/travel_info - краткая инфа о походе \n"
                                      "/members - участники сего алкотура \n"
                                      "/track - маршрут по горам (альфа версия) \n"
                                      "/menu - меню жратвы (пре-альфа версия) \n"
                                      "/bar - меню бара (бета версия) \n")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, я Гошин бот. Доступные команды, можно посмотреть тут /help")


@bot.message_handler(commands=["course"])
def course(message):
    c1 = privat_bank_course.get_usd_course_sale()
    c2 = privat_bank_course.get_usd_course_buy()
    bot.send_message(message.chat.id, f"Курс продажи доллара в привате: {c1} \n"
                                      f"Курс покупки доллара в привате: {c2}")


@bot.message_handler(commands=["travel_info"])
def course(message):
    bot.send_message(message.chat.id, "Значит так! Пиздуем 26го апреля в Черновцы. Там садимся на какой-то автобус"
                                      " и едем в сторону Белоберезки. "
                                      "Там тусуем по горам с финишем на резиденции Мультика. \n"
                                      "Потом снова прыгаем в автобус и едем назад в Черновцы, "
                                      "откуда, еще на одном автобусе, добираемся до Каменец-Подольского. "
                                      "В Каменце мы ночуем в гостиничке и на след день с утреца, "
                                      "мимо магазина едем на Бакоту, где и тюленим оставшиеся дни.\n"
                                      "4го мая возвращаемся в Каменец, где вечером садимся в поезд и тулим домой. ")


@bot.message_handler(commands=["members"])
def course(message):
    bot.send_message(message.chat.id, "В текущем алкотуре принимают участие:\n"
                                      "- ШШ \n"
                                      "- Лера \n"
                                      "- Гоша \n"
                                      "- Сако \n"
                                      "- Тарик \n"
                                      "- Инна \n"
                                      "- Степа \n"
                                      "- Олег \n"
                                      "- Наш новый(старый) алкодруг Артем")


@bot.message_handler(commands=["track"])
def course(message):
    photo = open('track.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, "FILEID")


@bot.message_handler(commands=["menu"])
def course(message):
    bot.send_message(message.chat.id, "Тут будет или екселька или скопирую сюда текстом.\n"
                                      "На данный момент пока не понятно шо мы жрем = )")


@bot.message_handler(commands=["bar"])
def course(message):
    bot.send_message(message.chat.id, "Алко меню: \n"
                                      "- Спирт \n"
                                      "- Водка \n"
                                      "- Пинаколада (self.production) \n"
                                      "- Самбука \n"
                                      "- Коньяк \n"
                                      "- Шот 'Мертвый Егерь' \n")


if __name__ == "__main__":
    bot.polling(none_stop=True)
