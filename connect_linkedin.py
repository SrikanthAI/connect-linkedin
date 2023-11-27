'''import requests
from linkedin_api import Linkedin

username=['nunesrikanth5121@gmail.com','srikanthn@pascalcase.com',]
password=['Sk19$868','Sk19$868']
apis = []
n=len(username)
for i in range(n):
    api = Linkedin(username[i], password[i])
    profile = api.get_profile()
    if profile:
        print('Account connected successfully!')
    else:
        print('Account not connected.')
    results = api.search_people('srikanth')
    print(len(results))
    for result in results:
        print(result['public_id'])
    break

# Now you can use the apis list to interact with each account'''





import requests
from bs4 import BeautifulSoup

first_name = "John"
last_name = "Doe"

url = f"https://www.linkedin.com/pub/dir/?first={first_name}&last={last_name}"

response = requests.get(url)
print(response)

soup = BeautifulSoup(response.content, 'html.parser')

for link in soup.find_all('a'):
    if "/in/" in link.get('href'):
        print(link.get('href').split('/')[2])





