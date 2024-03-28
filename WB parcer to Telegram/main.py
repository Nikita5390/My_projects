import time
from excel_reader import excel_reader
from parcer import ParseWB
from TG_message import SendMessageToTelegram


def parce_manager():
    while True:
        sku_data = excel_reader()
        for item in sku_data:
            parce_data = ParseWB(f"https://www.wildberries.ru/catalog/{item}/detail.aspx").parse()
            if parce_data[2] != 5:
                message = f"Товар:{parce_data[0]}; id:{parce_data[1]}; оценка:{parce_data[2]}; отзыв:{parce_data[3]}; текущий рейтинг:{parce_data[4]}"
                SendMessageToTelegram(message)

        time.sleep(150)


if __name__ == "__main__":
    parce_manager()
