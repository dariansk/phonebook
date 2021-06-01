from pprint import pprint
import re
import csv

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
# TODO 2: сохраните получившиеся данные в другой файл


def address_book(contacts_list: list):
    # регулярное выражение для телефонов
    phone = r'(\+7|8)(\s?)(\()?(\d+)(\)?)(\s?)(\-?)(\d+)?(\-?)(\d{2})?(\-?)(\d+)?(\s?)(\()?([добавочный.]+)?(\s)?(\d+)?(\))?'

    for contact in contacts_list[1:len(contacts_list)]:
        # если ФИО было через пробел, разбиваем:
        contact[0], contact[1], contact[2], *args = " ".join(contact[0:3]).split(' ')
        # преобразуем номер телефона:
        correct_phone = re.sub(phone, r"+7(\4)\8-\10-\12\13\15\17", contact[5])
        contact[5] = correct_phone
        # подчищаем пустые поля:
        if len(contact) > 7:
            del contact[7:]

    # боремся с дублями
    contacts_dict = {}
    for contact in contacts_list:
        if contact[0] not in contacts_dict.keys():
            contacts_dict[contact[0]] = contact[1:]
        else:
            for i, item in enumerate(contact[1:]):
                if contacts_dict[contact[0]][i - 6] == '':
                    contacts_dict[contact[0]][i - 6] = item

    address_book_list = []
    for key, value in contacts_dict.items():
        new_contact = [key]
        for v in value:
            new_contact.append(v)
        address_book_list.append(new_contact)

    with open("phonebook.csv", "w", encoding="utf8") as phone_book:
        data = csv.writer(phone_book, delimiter=',')
        data.writerows(address_book_list)

    return address_book_list


pprint(address_book(contacts_list))
