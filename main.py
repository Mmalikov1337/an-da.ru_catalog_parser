import bs4
import requests
import json
import time


def format_number_subcategory(num: int):
    if num < 10:
        return f'0{num}-{num}'
    else:
        return f'{num}-{num}'


def format_number_category(num: int):
    if num < 10:
        return f'00{num}-{num}'
    else:
        return f'0{num}-{num}'


def main():
    start_time = time.time()
    i = 2
    k = 1
    RESULT = []
    while i <= 2:
        temp_j = []
        j = 1
        if len(bs4.BeautifulSoup(requests.get(f'https://an-da.ru/catalog/{format_number_category(i)}/{format_number_subcategory(j)}/').text,
                                 "html.parser").find_all(class_="elementor-image-box-wrapper")) > 0:
            while j <= len(bs4.BeautifulSoup(requests.get(f'https://an-da.ru/catalog/{format_number_category(i)}/{format_number_subcategory(j)}/').text,
                                             "html.parser").find_all(class_="elementor-image-box-wrapper")):
                counter = 0
                temp_item = []

                for item in (bs4.BeautifulSoup(requests.get(f'https://an-da.ru/catalog/{format_number_category(i)}/{format_number_subcategory(j)}/').text,
                                               "html.parser").find_all(class_="elementor-image-box-wrapper")):
                                               print(f'{item.div.p}{bool(item.div.p)}')
                    temp_item.append({"index_item_k": counter, "title": str(item.div.h3.get_text()),"description": str(item.div.p.get_text()),"image":item.figure.img["src"] })  # INDEX{J}
                        

                    # print("-----------------------------------------------------------")
                    print(
                        f'----------------------------------------------------------- /{format_number_category(i)}/{format_number_subcategory(j)}/')

                    print({"index_item_k": counter, "title": str(item.div.h3.get_text()), "description": str(item.div.p.get_text()),"image":item.figure.img["src"] })
                    print("-----------------------------------------------------------")
                    counter += 1

                temp_j.append({"index_j": j, "CONTENT_J": temp_item})
                print(f'was \n\n{j} in j\n\n')
                j += 1
        else:
            while j < len(bs4.BeautifulSoup(requests.get(f'https://an-da.ru/catalog/{format_number_category(i)}/{format_number_subcategory(j)}/{format_number_subcategory(k)}').text,
                                            "html.parser").find_all(class_="elementor-image-box-wrapper")):
                counter = 0
                k = 1
                temp_item = []
                while k <= len(
                        bs4.BeautifulSoup(requests.get(f'https://an-da.ru/catalog/{format_number_category(i)}/{format_number_subcategory(j)}/{format_number_subcategory(k)}').text,
                                          "html.parser").find_all(class_="elementor-image-box-wrapper")):
                    for item in (
                            bs4.BeautifulSoup(
                                requests.get(
                                    f'https://an-da.ru/catalog/{format_number_category(i)}/{format_number_subcategory(j)}/{format_number_subcategory(k)} ').text,
                                "html.parser").find_all(class_="elementor-image-box-wrapper")):
                        temp_item.append(
                            {"index_item_k": counter, "title": str(item.div.h3.get_text()), "description": str(item.div.p.get_text()),"image":item.figure.img["src"] })  # INDEX{J}

                        print(
                            f'----------------------------------------------------------- /{format_number_category(i)}/{format_number_subcategory(j)}/{format_number_subcategory(k)}')
                        print({"index_item_k": counter, "title": str(item.div.h3.get_text()), "description": str(item.div.p.get_text()),"image":item.figure.img["src"] })
                        print(
                            "-----------------------------------------------------------")
                        counter += 1

                    temp_j.append({"index_j": j, "CONTENT_J": temp_item})
                    k += 1

                print(f'was \n\n{j} in j\n\n')
                j += 1

        print(f'was \n\n{i} in i\n\n')
        RESULT.append({"index_i": i, "CONTENT_I": temp_j})
        i += 1

    # print('\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    # print(json.dumps(RESULT, ensure_ascii=False))
    # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    with open('res.json', 'w', encoding='utf-8') as f:
        json.dump(RESULT, f, ensure_ascii=False)
    print(f'{(time.time() - start_time)}')


if __name__ == '__main__':
    main()
