#!/usr/bin/env python3 

from datetime import datetime
import os
import yaml


ARTICLES_PATH: str = 'articles'
TABLE_TITLE: str = '\n## Últimos artigos postados\n'


def get_article_yaml(article: str) -> dict:
    yaml_text: str = ''

    with open(f'{ARTICLES_PATH}/{article}', 'r') as file:
        for line in file.readlines()[1:]:
            if not line == '---\n':
                yaml_text += line
            else:
                break

    return yaml.safe_load(yaml_text)


def main() -> None:
    articles_list: list[str] = os.listdir(ARTICLES_PATH)
    main_table: list[dict] = []

    for article in articles_list:
        article_yaml: dict = get_article_yaml(article)
        info: dict = {}

        info['date']: str = article_yaml['date']
        info['perm_link']: str = 'posts/' + article.split('.')[0] + '.html'
        info['title']: str = article_yaml['title']

        main_table.append(info)

    main_table.sort(key=lambda article_info: datetime.strptime(article_info['date'], '%d/%m/%Y'), reverse=True)

    print(TABLE_TITLE)
    print('| **Data** | **Título** |')
    print('| :-: | ---------- |')

    for info in main_table:
        print(f'| {info["date"]} | [{info["title"]}]({info["perm_link"]}) |')


if __name__ == '__main__':
    main()
