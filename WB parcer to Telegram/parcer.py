import requests
import re
import requests
import csv
from models import Items, Feedback


class ParseWB:
    def __init__(self, url: str):
        self.seller_id = self.__get_seller_id(url)

    @staticmethod
    def __get_item_id(url: str):
        regex = "(?<=catalog/).+(?=/detail)"
        item_id = re.search(regex, url)[0]
        return item_id

    def __get_seller_id(self, url):
        response = requests.get(url=f"https://card.wb.ru/cards/v2/detail?nm={self.__get_item_id(url=url)}")
        seller_id = Items.parse_obj(response.json()["data"])
        return seller_id.products[0].supplierId

    def parse(self):
        page = 1
        self.__create_csv()
        while True:
            response = requests.get(
                f'https://catalog.wb.ru/sellers/v2/catalog?appType=1&curr=rub&dest=-1257786&sort=popular&spp=30&supplier={self.seller_id}&page={page}'
            )
            page += 1
            items_info = Items.parse_obj(response.json()["data"])
            if not items_info.products:
                break

            data = self.__feedback(items_info)
            return data

    @staticmethod
    def __feedback(item_model: Items):
        for product in item_model.products:
            url = f"https://feedbacks1.wb.ru/feedbacks/v1/{product.root}"
            res = requests.get(url=url)
            if res.status_code == 200:
                feedback = Feedback.model_validate(res.json())

                product.feedback_count = feedback.feedbackCountWithText
                product.valuation = feedback.valuation
                feedbacks = feedback.feedbacks
            return list[product.name, product.id, product.valuation, product.feedbacks.text, product.valuation]
