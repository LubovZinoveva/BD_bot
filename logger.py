import json

def load():
    with open('log.json', 'r', encoding = 'utf-8') as fh:
        BD = json.load(fh)
    return BD

def save(a):
    with open('log.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(a))
