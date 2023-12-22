import requests

word = input()

try:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    response = response.json()

    if response:
        w = response[0]['word']
        definition = response[0]['meanings'][0]["definitions"][0]["definition"]
        print(f"Definition of {w} is...\n")
        print(definition)

    else:
        print("Something is wrong with the API :(")

except Exception as excpt:
    print(f"Something is wrong, but not with the API: {excpt}")
