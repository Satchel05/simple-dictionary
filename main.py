import requests

try:
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/python"
    response = requests.get(url)

    if response:
        print("Success!")
    else:
        print("Something is wrong with the API :(")

except:
    print(f"Something is wrong, but not with the API")

