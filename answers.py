import requests

def t_answers(lat_index='V', index='5'):
    answers = []
    for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B']:
        file_url = 'http://sverh-zadacha.ucoz.ru/9/Skrelin/' + lat_index + '/8-' + i + '-' + index + '.js'
        resp = requests.get(file_url)
        resp.encoding = 'utf-8'
        s = resp.text.split('\r')[1].replace('ans0 = new Array(', '') \
            .replace(');', '').replace(' ', '').replace('\n', '')
        s.strip()
        answers.append(s)
    text_answers = "$array_answers = ["
    for x in answers:
        text_answers += "'" + x + "',"
    text_answers += '];'
    return text_answers

