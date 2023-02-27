import json




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





def SearchNum():
    directory = [{1: {"FirstName": "Иванов", "SecondName": "Иван", "Phone": "89340254185"}},
                 {2: {"FirstName": "Петров", "SecondName": "Петр", "Phone": "89528317456"}},]
    phones = input("Введите номер телефона: ")
    try:
        for i in directory:
            for p in i.values():
                if p.get("Phone") == phones:
                    print(p.get("FirstName"))
    except:
        print("Некорректно введен номер")

def SearchName():
    directory = [{1: {"FirstName": "Иванов", "SecondName": "Иван", "Phone": "89340254185"}},
                 {2: {"FirstName": "Петров", "SecondName": "Петр", "Phone": "89528317456"}}]
    name = input("Введите Фамилию: ")
    try:
        for i in directory:
            for p in i.values():
                if p.get("FirstName") == name:
                    print(p.get("SecondName"))
    except:
        print("Некорректно введена фамилия")












