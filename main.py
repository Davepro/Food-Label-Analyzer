from services.api_client import OpenFoodFactsClient
from services.nutrition_analyzer import NutritionAnalyzer
from services.meal_suggestion import MealSuggestionGenerator
from storage.food_log import FoodLog
from utils.validators import validate_barcode


def main():

    print("Program started")

    barcode = input("Enter product barcode: ")

    if not validate_barcode(barcode):
        print("Invalid barcode. Please enter 8 to 14 digits.")
        return

    api_client = OpenFoodFactsClient()
    product = api_client.fetch_product(barcode)

    if not product:
        print("Product not found.")
        return

    api_client = OpenFoodFactsClient()
    product = api_client.fetch_product(barcode)

    if not product:
        print("Product not found.")
        return

    product_name = product.get("product_name", "Unknown Product")
    nutrition = product.get("nutriments", {})
    allergens = product.get("allergens", "Not Available")

    print("\n========== PRODUCT DETAILS ==========")
    print("Name:", product_name)
    print("Allergens:", allergens)

    analyzer = NutritionAnalyzer()
    report = analyzer.analyze(nutrition)

    print("\n========== NUTRITION ANALYSIS ==========")

    for item in report:
        print("-", item)

    suggestion_generator = MealSuggestionGenerator()
    suggestions = suggestion_generator.suggest(report)

    print("\n========== HEALTHY SUGGESTIONS ==========")

    for suggestion in suggestions:
        print("-", suggestion)

    food_log = FoodLog()
    food_log.save_product(product_name)

    print("\nProduct saved successfully!")


if __name__ == "__main__":
    main()