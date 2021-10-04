from bs4 import BeautifulSoup as BS
import requests

# for i in ['1','2','3','4','5','6','7','8','9','10','A','B']:
problem = []
for i in ['1']:
    file_url = 'http://sverh-zadacha.ucoz.ru/9/Skrelin/V/8-' + i + '-5.htm'
    resp = requests.get(file_url)
    resp.encoding = 'utf-8'
    s = resp.text
    soup = BS(s, 'html.parser')

    ss = soup.findAll('div', 'ans')

    for st in ss:
        a = str(st)
        b = a.replace('<div class="ans">', '').replace('</b>', '') \
            .replace('<b>', '').replace('</div>', '') \
            .replace('<br/>', '').replace('\r', ' ').strip()
        problem.append(b)

    # soup = BS(s, 'lxml')
    razm = []
    for n in soup.select('input'):
        nn = n.next_sibling
        if nn is None:
            break
        n = str(nn)
        c = n.replace('\r\n', '')
        razm.append(c)
d = dict(zip(problem, razm))
for key in d:
    itog = "'" + key + "'=>'" + d[key] + "',"
    print(itog)
