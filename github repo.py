# Requesting response from html
import urllib.request
# used for scraping data from GitHub
from bs4 import BeautifulSoup
x = input("type your github handle")
response = urllib.request.urlopen(
    'https://github.com/' + x + '?tab=repositories'
)
soup = BeautifulSoup(response, 'html.parser')
a = soup.find('div', {'class': 'js-repo-list'})
list_tag = a.findAll('div', {'class': 'public source'})

# opening tags
for tag in list_tag:
    tags = tag.find('a')
    print(tags.string.strip())
    print('\n')

print("These are the repositories found. \
    Type the exact name of repository u want to download")
print('\n')
y = input()

for tag in list_tag:
    tags = tag.find('a')
    if(tags.string.strip() == y):
        break

# dowloading the repo.
if(tags.string.strip() == y):
    urllib.request.urlretrieve(
        'https://github.com/%s/%s/archive/master.zip' % (
            x.strip(), tags.string.strip()
        ),
        'repository.zip'
    )
    z = input('The repos2itory is successfully downloaded\
     to your current default directory')
else:
    p = input("no such repository found")
