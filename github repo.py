import urllib.request
import shutil
import os
from bs4 import BeautifulSoup
x=input("type your github handle")
response=urllib.request.urlopen('https://github.com/'+x+'?tab=repositories')
soup=BeautifulSoup(response,'html.parser')
a=soup.find('div',{'class':'js-repo-list'})
list_tag=a.findAll('div',{'class':'public source'})
print("These are the repositories found.Type the exact name of repository u want to download") 
print('\n')
    
for tag in list_tag:
    tags=tag.find('a')
    print(tags.string.strip())
    print('\n')
    
y=input()

for tag in list_tag:
    tags=tag.find('a')
    if(tags.string.strip()==y):
        break

if(tags.string.strip()==y):
    urllib.request.urlretrieve('https://github.com/'+x.strip()+'/'+tags.string.strip()+'/archive/master.zip','repository.zip')
    print('The repository is successfully downloaded to your current default directory')
    x=input()
else:
    print("no such repository found")
    x=input()
    
