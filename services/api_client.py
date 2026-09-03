import requests


class OpenFoodFactsClient:

    BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

    def fetch_product(self, barcode):

        try:
            url = f"{self.BASE_URL}/{barcode}.json"

            headers = {
                "User-Agent": "FoodLabelAnalyzer/1.0"
            }

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()

            if data.get("status") == 1:
                return data.get("product")
            else:
                raise ValueError("Product not found.")

        except requests.exceptions.RequestException as e:
            print(f"Network Error: {e}")
            return None

        except ValueError as e:
            print(e)
            return None
