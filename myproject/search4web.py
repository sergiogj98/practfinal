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

    letras= letters.split(sep=',')
    phrases = phrase.split(sep='.')

    rst=[]
    phra=[]
    results=[]
    statistics=[]
    for phr in phrases:
        for let in letras:
            if phr != "":
                phra.append(phr)
                rst.append(set(let).intersection(set(phr)))
    results.append(phra)
    results.append(rst)

    return results,statis

def log_request(req: 'flask_request', res: str) -> None:
    """ logger for web operations """
    with open('search.log','a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

def contarElementosLista(lista):
    counter=Counter(lista)
    if len(lista)>3 :
        first, second, third, *_ = counter.most_common()
        statis = [first, second, third]
    elif len(lista) == 3:
        first, second, third= counter.most_common()
        statis = [first, second, third]
    elif len(lista)==2:
        first, second= counter.most_common()
        statis = [first, second]
    elif len(lista)==1:
        first= counter.most_common()
        statis = [first]

    return statis
