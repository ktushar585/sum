import requests
import urllib.request
from bs4 import BeautifulSoup
import requests, warnings

def get_questions(in_url):
    res = urllib.request.urlopen(in_url)
    soup = BeautifulSoup(res.read(), 'html.parser')
    get_names = lambda f: [v for k,v in f.attrs.items() if 'label' in k]
    get_name = lambda f: get_names(f)[0] if len(get_names(f))>0 else 'unknown'
    all_questions = soup.form.findChildren(attrs={'name': lambda x: x and x.startswith('entry.')})
    return {get_name(q): q['name'] for q in all_questions}

TEST_FORM_URL = "https://docs.google.com/forms/d/1DWvmWjz0WN9FLheU_aIAlc8PM50cUu7AMY7yw7QoWuQ/viewform"

anno_questions = get_questions(TEST_FORM_URL)

url = "https://docs.google.com/forms/d/1DWvmWjz0WN9FLheU_aIAlc8PM50cUu7AMY7yw7QoWuQ/formResponse"
z=0


data = {
    "anno_questions['Name']": "mayank",
    "anno_questions['Roll Number']": "12345",
    "anno_questions['unknown']": "Yes",
    "anno_questions['Link to github repo/pastebin where I can see your script']": "https://docs.google.com/forms/d/1DWvmWjz0WN9FLheU_aIAlc8PM50cUu7AMY7yw7QoWuQ/edit",
}
while(z<5):
    print(data)
    result = requests.post(url,data)
    print(result)
    z=z+1