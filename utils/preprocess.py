def validate_input(input_data):
    if not input_data.get("theme") or not input_data.get("style"):
        raise ValueError("Theme and style are required fields.")
    print("Input validated.")
    return True
