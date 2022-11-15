from logger import load, save

def delete_data(id):
    data = load()
    for el in data:
        if el.get('id') == id:
            data.remove(el)
    save(data)

def data_replacement(info):
    data = load()
    for el in data:
        if el.get('id') == info[0]:
            el[info[1]] = info[2]
    save(data)

def add_new_people(new_man):
    bd = load()
    result = []
    for e in bd:
        result.append(e)
    result.append(new_man)
    save(result)
