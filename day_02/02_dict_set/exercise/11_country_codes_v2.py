running = True
while True:
    country_codes = {
        "PH": "Philippines",
        "US": "United States",
        "JP": "Japan",
        "KR": "Korea"
    }

# TODO: Print the country for the given country code
    code_choice = input(f"Enter a country code: ")
    print(country_codes.get(code_choice, "Enter a valid code."))
