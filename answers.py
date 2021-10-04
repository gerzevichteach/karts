import wget
import requests

# for i in ['1','2','3','4','5','6','7','8','9','10','A','B']:
answers =[]
for i in ['1','2','3','4','5','6','7','8','9','10','A','B']:
    file_url = 'http://sverh-zadacha.ucoz.ru/9/Skrelin/V/8-'+i+'-5.js'
    resp = requests.get(file_url)
    resp.encoding = 'utf-8'
    s = resp.text.split('\r')[1].replace('ans0 = new Array(','')\
        .replace(');','').replace(' ','').replace('\n','')
    s.strip()
    answers.append(s)
print(answers)


