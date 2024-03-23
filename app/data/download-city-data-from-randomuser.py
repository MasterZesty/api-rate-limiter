import requests

def download_file(country_code):
    url = f"https://raw.githubusercontent.com/RandomAPI/Randomuser.me-Node/master/api/1.4/data/{country_code}/lists/cities.txt"
    response = requests.get(url)
    with open(f"{country_code}-cities.txt", 'wb') as file:
        file.write(response.content)

countries = ["AU", "BR", "CA", "CH", "DE", "DK", "ES", "FI", "FR", "GB", "IE", "IN", "IR", "LEGO", "MX", "NL", "NO", "NZ", "RS", "TR", "UA", "US"]
for country in countries:
    download_file(country)
