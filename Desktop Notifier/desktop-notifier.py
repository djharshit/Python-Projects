#!/usr/bin/env python3

"""
Desktop Notifier using Python

"""
# Importing requireed modules
import time
import random
import plyer
import requests

# Generate 3 facts about random numbers
for i in range(5):
    # Generate a random number between 1 and 1000
    no = random.randint(1, 1000)

    # Request the fact about the number
    url = f'https://numbersapi.p.rapidapi.com/{no}/math'
    query = {'fragment':'true','json':'true'}

    head = {
        'x-rapidapi-host': 'numbersapi.p.rapidapi.com',
        'x-rapidapi-key': '311c281d5dmshd8fd120724a79bfp166364jsn4b3e36fce9c8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36'
        }

    res = requests.get(url=url, headers=head, params=query)
    data = res.json()

    # Send the notification to the desktop
    plyer.notification.notify(title=f'Random Number Fact: {no}',
                              message=data['text'],
                              app_icon='pic.ico',
                              timeout=5
                              )
    # 10 sec delay before sending next notification
    time.sleep(10)
