

import telebot
import openai

openai.api_key = "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" #اكتب هنا الايبي

bot = telebot.TeleBot(token="6227855349:AAGDROtahkYTVZ1nNCAoWGaU9k-ieMHYQzQ") # توكن البوت

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,#عدد الحروف
        n=1,
        temperature=0.5,
)

    return response["choices"][0]["text"]

bot.set_my_commands([
    {
        "command": "/chatgpt", # الاستارت
        "description": "*مرحبا بك في عالم الذكاء الاصطناعي!" 
    }
])

@bot.message_handler(func=lambda message: True)
def handle_message(message):

    AUTHORIZED_USER_IDS = ['']
    text = message.text

    response = generate_response(text)

    bot.send_message(chat_id=message.chat.id, text=response)
    
bot.polling()