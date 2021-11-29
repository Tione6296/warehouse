import requests
from bs4 import  BeautifulSoup

res=requests.get('https://web.lobi.co/game/houkai_gakuen/group/2dcc2f909a5a9d7d66c1cc7d2748db84bd3c76a9/chat/755235212547334145').text
soup = BeautifulSoup(res,'html.parser')
title=soup.find('title').get_text()
print(title)
for script in soup(["script","style"]):
    script.decompose()

text=soup.get_text()
lines=[line.strip() for line in text.splitlines()]
text="\n".join(line for line in lines if line)

print(text)
'''
quote_elms = soup.find_all('div', {'class': 'body'})
lines=[line.strip() for line in quote_elms]
print(quote_elms)
'''
f=open('lobikunsyobs4.txt','w',encoding='UTF-8')
f.writelines(text)
f.close()
