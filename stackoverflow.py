# ---------------------------------------------------------------------------------
# Script to get most recent unanswered Python questions on Stackoverflow.
# Author Hemant Kumar <hkbiet@gmail.com>
# ---------------------------------------------------------------------------------
import requests

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for index, data in enumerate(response.json()['items']):
    if 'python' in data['tags'] and data['answer_count'] == 0:
        print(index, data['title'])
        print(data['link'])
        print()