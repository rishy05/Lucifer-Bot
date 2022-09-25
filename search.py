#search.py

import requests 
import json


def browse(term):
    term.replace(' ', '+')
    url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={term}"

    headers = {
	"X-User-Agent": "desktop",
	"X-Proxy-Location": "IN",
	"X-RapidAPI-Key": 'API KEY',
	"X-RapidAPI-Host": "google-search3.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    content = json.loads(response.text)
    return(content['results'][0]['title'], content['results'][0]['link'])