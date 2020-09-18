import bs4
import requests
import json
import time


def main():
    start_time = time.time()
    i = 2
    k = 1
    RESULT = []
    while i <= 4:
        temp_j = []
        j = 1
        if len(bs4.BeautifulSoup(requests.get(f'https://an-da.ru/catalog/00{i}-{i}/0{j}-{j}/').text,
                                 "html.parser").find_all(class_="elementor-image-box-content")) > 0:
            while j <= len(bs4.BeautifulSoup(requests.get(f'https://an-da.ru/catalog/00{i}-{i}/0{j}-{j}/').text,
                                            "html.parser").find_all(class_="elementor-image-box-content")):
                counter = 0
                temp_item = []

                for item in (bs4.BeautifulSoup(requests.get(f'https://an-da.ru/catalog/00{i}-{i}/0{j}-{j}/').text,
                                               "html.parser").find_all(class_="elementor-image-box-content")):
                    temp_item.append(
                        {"index_item": counter, "title": str(item.h3), "description": str(item.p), })  # INDEX{J}

                    print("-----------------------------------------------------------")
                    print({"index_item": counter, "title": str(item.h3), "description": str(item.p)})
                    print("-----------------------------------------------------------")
                    counter += 1

                temp_j.append({"index_j": j, "CONTENT_J": temp_item})
                print(f'was \n\n{j} in j\n\n')
                j += 1
        else:
            while j < len(bs4.BeautifulSoup(requests.get(f'https://an-da.ru/catalog/00{i}-{i}/0{j}-{j}/0{k}-{k}').text,
                                            "html.parser").find_all(class_="elementor-image-box-content")):
                counter = 0
                k = 1
                temp_item = []
                while k <= len(
                        bs4.BeautifulSoup(requests.get(f'https://an-da.ru/catalog/00{i}-{i}/0{j}-{j}/0{k}-{k}').text,
                                          "html.parser").find_all(class_="elementor-image-box-content")):
                    for item in (
                            bs4.BeautifulSoup(
                                requests.get(f'https://an-da.ru/catalog/00{i}-{i}/0{j}-{j}/0{k}-{k}').text,
                                "html.parser").find_all(class_="elementor-image-box-content")):
                        temp_item.append(
                            {"index_item_k": counter, "title": str(item.h3), "description": str(item.p), })  # INDEX{J}

                        print("-----------------------------------------------------------")
                        print({"index_item_k": counter, "title": str(item.h3), "description": str(item.p)})
                        print("-----------------------------------------------------------")
                        counter += 1

                    temp_j.append({"index_j": j, "CONTENT_J": temp_item})
                    k += 1

                print(f'was \n\n{j} in j\n\n')
                j += 1

        print(f'was \n\n{i} in i\n\n')
        RESULT.append({"index_i": i, "CONTENT_I": temp_j})
        i += 1

    print('\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(json.dumps(RESULT, ensure_ascii=False))
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    with open('res.json', 'w', encoding='utf-8') as f:
        json.dump(RESULT, f, ensure_ascii=False)
    print(f'{(time.time() - start_time)}')


if __name__ == '__main__':
    main()
