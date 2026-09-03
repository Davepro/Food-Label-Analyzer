import re


def validate_barcode(barcode):

    pattern = r"^\d{8,14}$"

    if re.match(pattern, barcode):
        return True

    return False


def clean_product_name(name):

    cleaned_name = re.sub(r"[^a-zA-Z0-9\s]", "", name)

    return cleaned_name.strip()