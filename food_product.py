class FoodProduct:
    def __init__(self, name, ingredients, nutrition, allergens):
        self.name = name
        self.ingredients = ingredients
        self.nutrition = nutrition
        self.allergens = allergens

    def display_info(self):
        print(f"\nProduct: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Nutrition: {self.nutrition}")
        print(f"Allergens: {self.allergens}")

        