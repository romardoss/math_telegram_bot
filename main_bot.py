import telebot
import token_bot
import help_command
import problems
import api_module as api
import check_input

bot=telebot.TeleBot(token_bot.token)


def g(number):                #to format the text to ```text```
  return f'`{str(number)}`'

@bot.message_handler(commands=['start'])
def start_message(message):
  print(message.from_user.username + ' firstly using a bot')
  bot.send_message(message.chat.id,"Введи любий вираз типу '2+3' і я його порахую. тикай /help для всіх фішок")

@bot.message_handler(commands=['help'])
def help_message(message):
    print(message.from_user.username + ' is searching a bot')
    bot.send_message(message.chat.id, help_command.help_message)

@bot.message_handler(commands=['all_functions'])
def all_message(message):
    print(message.from_user.username + ' is searching a bot')
    bot.send_message(message.chat.id, help_command.all_functions, parse_mode='MarkdownV2')

@bot.message_handler(commands=['compare'])
def compare_calc(message):
    print(message.from_user.username + ' is using a bot')
    if check_the_user(message):
        return 0
    bot.send_message(message.chat.id, g(problems.compare(message)), parse_mode='MarkdownV2')




@bot.message_handler(content_types=['text'])
def text_calc(message):
    print("("+str(message.from_user.username)+")" + ' is using a bot') # перевірка користувача
    print(message.text)
    
    checked_input = check_input.main(message.text)
    bot.send_message(message.chat.id, g(api.main(checked_input)), parse_mode='MarkdownV2')

    
bot.infinity_polling()
