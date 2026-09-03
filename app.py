import streamlit as st

from services.api_client import OpenFoodFactsClient
from services.nutrition_analyzer import NutritionAnalyzer
from services.meal_suggestion import MealSuggestionGenerator
from storage.food_log import FoodLog
from utils.validators import validate_barcode


st.set_page_config(
    page_title="Food Label Analyzer",
    page_icon="🍔",
    layout="centered"
)

st.title("🍔 Food Label Analyzer")
st.write("Analyze food products using their barcode.")

barcode = st.text_input("Enter Product Barcode")

if st.button("Analyze Product"):

    if not validate_barcode(barcode):
        st.error("Please enter a valid barcode (8-14 digits).")

    else:
        api_client = OpenFoodFactsClient()
        product = api_client.fetch_product(barcode)

        if not product:
            st.error("Product not found.")

        else:
            product_name = product.get(
                "product_name",
                "Unknown Product"
            )

            nutrition = product.get("nutriments", {})
            allergens = product.get(
                "allergens",
                "Not Available"
            )

            st.subheader("📦 Product Details")

            st.write(f"**Name:** {product_name}")
            st.write(f"**Allergens:** {allergens}")

            analyzer = NutritionAnalyzer()
            report = analyzer.analyze(nutrition)

            st.subheader("📊 Nutrition Analysis")

            for item in report:
                st.write(f"✅ {item}")

            suggestion_generator = MealSuggestionGenerator()
            suggestions = suggestion_generator.suggest(report)

            st.subheader("🥗 Healthy Suggestions")

            for suggestion in suggestions:
                st.write(f"• {suggestion}")

            food_log = FoodLog()
            food_log.save_product(product_name)

            st.success("Product saved successfully!")