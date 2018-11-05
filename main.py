import telebot, config, privat_bank_course

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "Доступные команды: \n"
                                      "/help - описание доступных команд \n"
                                      "/start - Приветствие \n"
                                      "/course - текущий курс доллара в приват банке")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, я Гошин бот. Буду помогать ему чем смогу")


@bot.message_handler(commands=["course"])
def course(message):
    c1 = privat_bank_course.get_usd_course_sale()
    c2 = privat_bank_course.get_usd_course_buy()
    bot.send_message(message.chat.id, f"Курс продажи доллара в привате: {c1} \n"
                                      f"Курс покупки доллара в привате: {c2}")


if __name__ == "__main__":
    bot.polling()
