from bs4 import BeautifulSoup as bs
import requests



def problems(lat_index='V', index='5'):
    problem = []
    itog = ''
    # Вопросы карточек одинаковы
    file_url = 'http://sverh-zadacha.ucoz.ru/9/Skrelin/' + lat_index + '/8-1-' + index + '.htm'
    resp = requests.get(file_url)
    resp.encoding = 'utf-8'
    s = resp.text
    soup = bs(s, 'html.parser')

    ss = soup.findAll('div', 'ans')

    for st in ss:
        a = str(st)
        b = a.replace('<div class="ans">', '').replace('</b>', '') \
            .replace('<b>', '').replace('</div>', '') \
            .replace('<br/>', '').replace('\r', ' ').strip()
        problem.append(b)
    print(problem)

    razm = []
    for n in soup.select('input'):
        nn = n.next_sibling
        if nn is None:
            break
        n = str(nn)
        c = n.replace('\r\n', '')
        razm.append(c)
    print(razm)
    d = dict(zip(problem, razm))
    for key in d:
        itog += "'" + key + "'=>'" + d[key] + "',"
    return "$problems = [" + itog + "];"
