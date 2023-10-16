import requests

#browses the api for the word by taking in word from the search_definition fucntion
def get_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        if data:
            meanings = data[0]['meanings']
            definitions = []
            for meaning in meanings:
                definitions.append(f"{word}\n• Meaning: {meaning['partOfSpeech']}\nDefinition: {meaning['definitions'][0]['definition']}\n")
            return '\n'.join(definitions)
        return "No definition found."

#Searches for the word by taking in entry
def search_definition(entry):
    word = entry
    definition = get_definition(word)
    return definition

