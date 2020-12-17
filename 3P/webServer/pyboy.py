import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '847365049:AAHP_qPi8e_bePCWY8OVOx-vChb4Qk6OmX4'
    bot_chatID = '1305712253'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext("Testing Telegram bot")
print(test)