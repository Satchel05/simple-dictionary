import requests

word = input()

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
response = requests.get(url)

if response.status_code != 200:
    print("Not a word")
else:
    response = response.json()
    w = response[0]['word']
    definition = response[0]['meanings'][0]["definitions"][0]["definition"]
    print(f"Definition of {w} is...\n")
    print(definition)
