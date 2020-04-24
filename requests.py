import requests
import urllib.request
from bs4 import BeautifulSoup
import requests, warnings
# THIS IS THE REQUIRED CODE
import requests

url = "https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/formResponse"
z=0


data = {
    'entry.1156409': "Tushar kumar",
    'entry.210055283': "190916",
    'entry.192452008': "Yes",
    'entry.446099277': "https://github.com/ktushar585/sum/blob/master/requests.py",
}

while(z<100):
    print(data)
    result = requests.post(url,data)
    print(result)
    z=z+1


#BELOW IS THE WHOLE CODE ALONG WITH EXTRACTING THE QUESTION ID'S AND FILING THE FORM TOO BUT THIS CODE IS EXECUTING SUCCESSFULLY 
#BUT THE FORM IS NOT FILING ,THEREFORE I HAD TO EXTRACT THE QUESTION ID'S SEPARATELY AND THE FILL IN THE GOOGLE FORM .



# def get_questions(in_url):
#     res = urllib.request.urlopen(in_url)
#     soup = BeautifulSoup(res.read(), 'html.parser')
#     get_names = lambda f: [v for k,v in f.attrs.items() if 'label' in k]
#     get_name = lambda f: get_names(f)[0] if len(get_names(f))>0 else 'unknown'
#     all_questions = soup.form.findChildren(attrs={'name': lambda x: x and x.startswith('entry.')})
#     return {get_name(q): q['name'] for q in all_questions}

# TEST_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/viewform"

# anno_questions = get_questions(TEST_FORM_URL)

# url = "https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/formResponse"
# z=0


# data = {
#     "anno_questions['Name']": "Tushar kumar ",
#     "anno_questions['Roll Number']": "190916",
#     "anno_questions['unknown']": "Yes",
#     "anno_questions['Link to github repo/pastebin where I can see your script']": "https://github.com/ktushar585/sum/edit/master/requests.py",
# }
# while(z<100):
#     print(data)
#     result = requests.post(url,data)
#     print(result)
#     z=z+1
