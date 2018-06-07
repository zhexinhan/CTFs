#!/usr/bin/python3.6

import requests

message_url = "http://www.wechall.net/challenge/training/programming1/index.php?action=request"
destination_url = "http://www.wechall.net/challenge/training/programming1/index.php?answer="

with requests.session() as session:
    # # Ways to use payload
    # payload = {
    #     'username': 'username',
    #     'password': 'password'
    # }
    # response = session.post(url=message_url, data=payload)

    # Retrieve this value by inspecting the page,
    # then Application -> Storage -> Cookies
    cookies = {
        'WC': '10513720-41275-Mvbfq9B26p83c12O'
    }
    response = session.get(url=message_url, cookies=cookies)
    print("Response message is " + response.text)

    response = session.get(url=destination_url + response.text, cookies=cookies)
    # print(response.content)