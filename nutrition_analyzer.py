class NutritionAnalyzer:

    def analyze(self, nutrition_data):

        report = []

        sugar = nutrition_data.get("sugars_100g", 0)
        fat = nutrition_data.get("fat_100g", 0)
        salt = nutrition_data.get("salt_100g", 0)
        calories = nutrition_data.get("energy-kcal_100g", 0)

        if sugar > 22.5:
            report.append("High Sugar Content")
        elif sugar > 5:
            report.append("Moderate Sugar Content")
        else:
            report.append("Low Sugar Content")

        if fat > 17.5:
            report.append("High Fat Content")
        elif fat > 3:
            report.append("Moderate Fat Content")
        else:
            report.append("Low Fat Content")

        if salt > 1.5:
            report.append("High Salt Content")
        elif salt > 0.3:
            report.append("Moderate Salt Content")
        else:
            report.append("Low Salt Content")

        if calories > 400:
            report.append("High Calorie Food")
        elif calories > 150:
            report.append("Moderate Calorie Food")
        else:
            report.append("Low Calorie Food")

        return report