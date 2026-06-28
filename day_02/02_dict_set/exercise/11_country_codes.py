# TODO: Add more country codes
running = True
while running:
    code_choice = input (f"Enter a country code: ")
    country_codes = {
        "PH": "Philippines",
        "US": "United States",
        "JP": "Japan",
        "KR": "Korea"
    }
    if code_choice in country_codes:
        print(country_codes[code_choice])
    else:
        print("Choose a different code.")
