import telegram
import configparser
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
        #Message to display when the bot starts
        keyboard = [[InlineKeyboardButton("💻 • Developer", url="https://t.me/stehack")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
      
        update.message.reply_text(text=f'''
👋 | **ʜɪ @{update.message.from_user.username}!**
💬 › ꜱᴇɴᴅ ᴀ ᴍᴇꜱꜱᴀɢᴇ ʜᴇʀᴇ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ!
'''.replace("@None","@//"),parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=reply_markup)
   

def send(update, context):
    #When a message is sent to the bot, it forwards the message to the owner
    context.bot.forward_message(chat_id=uidown, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    sendmex = (f"[`{update.message.chat_id}`] - @{update.message.from_user.username}\n\n🗣 | _For reply to user, reply to this message!_").replace("@None", "@//")
    context.bot.send_message(chat_id=uidown, text=sendmex, parse_mode=telegram.ParseMode.MARKDOWN)   
    
        
def reply(update, context):
    #When the owner reply to the bot's message, it forwards the message to the user that has sent it
    if str(update.message.chat_id) == str(uidown):
        if str(update.message.reply_to_message.from_user.id) == botid:
            try:
                string = str(update.message.reply_to_message.text)[1:(str(update.message.reply_to_message.text).find("] - "))]
                print(string)      
                context.bot.send_message(chat_id=string, text = "» " + update.message.text)
            except:
                if "For reply to user, reply to this message!" in update.message.reply_to_message.text:
                    context.bot.send_message(chat_id=uidown, text = "**⚠️ | There was an error! Message hasn't been sent!**", parse_mode=telegram.ParseMode.MARKDOWN)

            
def main():
    #Main function
    config = configparser.ConfigParser()
    config.read('config.ini')
    TOKEN = config['Config']['TOKEN']

    global uidown
    uidown = config['Config']['YOUR_USER_ID']

    #Get bot's UserId
    global botid
    botid = (TOKEN.split(":"))[0]

    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.chat(uidown) & Filters.reply & Filters.all, reply))
    dp.add_handler(MessageHandler(Filters.all & ~Filters.command, send))
    updater.start_polling()
    updater.idle()
    
    
if __name__ == '__main__':
    main()
