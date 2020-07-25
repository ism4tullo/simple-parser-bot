from telegram.ext import Updater, CommandHandler, MessageHandler #defaut python-telegram-bot modules
from bs4 import BeautifulSoup #bs4 for parsing
import requests  #for http requests


DOMAIN = 'https://mp3mob.net/'   #Site's Domain

URL = 'https://mp3mob.net/best/month'  #URL from page for parsing


def start(update, context):
    update.message.reply_text('Started')


def check():
	#I am not robot :3
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    #selecting needed html classes
    items = soup.select('div.track-item fx-row fx-middle js-item')  
    items = soup.select_one('a.track-dl').get('href')
    
    return  DOMAIN + items 
   

def parse(update, context):
	update.message.reply_text(check())


updater = Updater('1311406717:AAFloTGB6EerhH1Q9lGHGBXrwR2Tm0wtSFI',  #TOKEN from @Botfather
		use_context=True) 

#Commands with '/' 
updater.dispatcher.add_handler(CommandHandler('start', start)) #if text = /start
updater.dispatcher.add_handler(CommandHandler('parse', parse)) #if text = /parse

#Run bot
updater.start_polling()
updater.idle()

