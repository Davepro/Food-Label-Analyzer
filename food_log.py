import json
import os


class FoodLog:

    FILE_NAME = "storage/food_log.json"

    def save_product(self, product_name):

        data = []

        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []

        data.append(product_name)

        with open(self.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def load_products(self):

        if not os.path.exists(self.FILE_NAME):
            return []

        try:
            with open(self.FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []