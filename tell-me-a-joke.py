import requests

apology = 'Sorry! Couldn\'t retrieve an awesome Chuck Norris Joke for you.'

try:
    response = requests.get('https://api.chucknorris.io/jokes/random')
    if response:
        joke = response.json()
        print(joke['value'])
    else:
        print(apology)
except:
    print(apology)