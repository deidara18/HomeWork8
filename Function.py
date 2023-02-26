import json


directory = [{}]


def save():
    sprav = 'phone.json'
    with open(sprav, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(directory, ensure_ascii=False))
    print("Новая информация сохранена в справочник, phone.json")



def load():
    with open("phone.json", "r", encoding="utf-8") as fh:
        directory = json.load(fh)
    print("Справочник был успешно загружен")
    return directory

try:
    with open("phone.json", "r", encoding="utf-8") as fh:
        directory = json.load(fh)
    print("Справочник был успешно загружен")
except:
    directory.append("")


def add_info():
    info = input("Введите информацию для добавления")
    return directory.append(info)


def all_info():
    print("Информация справочника", directory)
    return directory



def del_info():
    try:
        info = input("Введите информацию для удаления : ")
        return directory.remove(info)
    except:
        print("Не правильно введена информация")



def Search():
    directory = [{"FirstName": "Иванов", "SecondName": "Иван", "Phone": "89340254185"}, {"FirstName": "Петров", "SecondName": "Петр", "Phone": "89528317456"}]
    name1 = input("Введите имя: ")
    for k, v in directory:
        if directory[k]['SecondName'] == name1:
            print(directory[k]['Phone'])
            if directory[v]["FirstName"] == name1:
                print(directory[v]['Phone'])
                return directory.append(name1)
            else:
                print('нет такого значения')















