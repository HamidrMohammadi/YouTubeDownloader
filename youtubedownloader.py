
pip install pyTelegramBotAPI pytube

import telebot
from pytube import YouTube

bot = telebot.TeleBot('TelegramBotTokenhere')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the YouTube Downloader Bot! Send me a YouTube video link to download.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    try:
        yt = YouTube(message.text)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        stream.download()
        bot.send_message(message.chat.id, f"Video '{yt.title}' has been downloaded successfully!")
    except Exception as e:
        bot.send_message(message.chat.id, f"An error occurred: {e}")

bot.polling()