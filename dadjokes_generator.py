import requests
import random


def generate_jokes():
    the_jokes = input("What do you want to hear about? ")
    url = "https://icanhazdadjoke.com/search"
    res = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": the_jokes},
    )
    data = res.json()
    if data["total_jokes"] == 0:
        print(f"Sorry I don't have any jokes about {the_jokes}")
    elif data["total_jokes"] == 1:
        print(f'I have got one joke for {the_jokes}, here it is: {(jokes["joke"] for jokes in data["results"])}')
    elif data["total_jokes"] > 1:
        print(f'I have got {data["total_jokes"]} jokes about that, here is one: {random.choice([jokes["joke"] for jokes in data["results"]])}')


print("Dad Jokes Generator")
i = 0
while i == 0:
    generate_jokes()
    replay = input("Do you want to try another one?(yes/no) ")
    if replay == "no":
        print("Ok, Thanks for hearing me")
        break
    elif replay == "yes":
        i = 0
