import re
from collections import Counter
def search4vowels(word: str) -> set:
    """ Return any vowels found in word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """ Return any letters found in phrase """
    return set(letters).intersection(set(phrase))

def search4letters_upgrade(phrase: str, letters: str = 'aeiou') -> set:
    """ Return any letters found in phrase """
    words=re.split('\W+',phrase)
    statis = contarElementosLista(words)

    phrases = phrase.split(sep='.')
    rst=[]
    phra=[]
    results=[]
    statistics=[]
    for phr in phrases:
        if phr != "":
            phra.append(phr)
            rst.append(set(letters).intersection(set(phr)))
    results.append(phra)
    results.append(rst)

    return results,statis

def log_request(req: 'flask_request', res: str) -> None:
    """ logger for web operations """
    with open('search.log','a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

def contarElementosLista(lista):
    counter=Counter(lista)
    first, second, third, *_ = counter.most_common()
    statis=[first,second,third]
    return statis
