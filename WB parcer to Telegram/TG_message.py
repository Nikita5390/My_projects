import requests
from Secret_key import BOT_KEY, ChatID

TelegramBotCredential = BOT_KEY   #BotKEY
ReceiverTelegramID = ChatID  #chatID


def SendMessageToTelegram(message):
    try:
        Url = "https://api.telegram.org/bot" + str(TelegramBotCredential) + "/sendMessage?chat_id=" + str(
            ReceiverTelegramID)

        textdata = {"text": message}
        response = requests.request("POST", Url, params=textdata)
    except Exception as e:
        message = str(e) + ": Exception occur in SendMessageToTelegram"
        print(message)
