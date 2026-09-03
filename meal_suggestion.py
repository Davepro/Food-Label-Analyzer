class MealSuggestionGenerator:

    def suggest(self, analysis_report):

        suggestions = []

        if "High Sugar Content" in analysis_report:
            suggestions.append(
                "Consider fruits, unsweetened yogurt, or low-sugar snacks."
            )

        if "High Fat Content" in analysis_report:
            suggestions.append(
                "Try grilled foods, vegetables, or lean protein options."
            )

        if "High Salt Content" in analysis_report:
            suggestions.append(
                "Choose fresh foods and reduce processed snacks."
            )

        if "High Calorie Food" in analysis_report:
            suggestions.append(
                "Consider lower-calorie alternatives such as salads or fruit bowls."
            )

        if not suggestions:
            suggestions.append(
                "This product appears relatively balanced. Enjoy in moderation."
            )

        return suggestions