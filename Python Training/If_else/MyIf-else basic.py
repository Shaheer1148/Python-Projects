a = int(input("Please Enter your Age: "))
print("Your Age is: ", a)

if(a>18):
    print("You can drive")
else:
    print("You can't drive")

# Function to check the country code
def check_country(b):
    country_code = b[:2]  # Get the first two digits of the phone number
    
    if country_code == "91":
        return "India"
    elif country_code == "49":
        return "Germany"
    elif country_code == "1":
        return "USA or Canada"
    elif country_code == "44":
        return "United Kingdom"
    elif country_code == "33":
        return "France"
    elif country_code == "81":
        return "Japan"
    else:
        return "Country code not recognized"

# Input: phone number
b = input("Enter the phone number with country code: ")
country = check_country(b)

print(f"Country: {country}")

