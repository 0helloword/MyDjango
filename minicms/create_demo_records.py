#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
create some records for demo database
'''

from minicms.wsgi import *
from news.models import Column, Article


def main():
    columns_urls = [
      ('体育新闻', 'sports'),
      ('社会新闻', 'society'),
      ('科技新闻', 'tech'),
       ('娱乐新闻', 'recreation'),
      ('房产新闻', 'house'),
      ('生活新闻', 'live'),
    ]

    for column_name, url in columns_urls:
        c = Column.objects.get_or_create(name=column_name, slug=url,intro='新闻')[0]
        print(c)
        # 创建 10 篇新闻
        for i in range(1, 11):
            article = Article.objects.get_or_create(
                title='{}_{}'.format(column_name, i),
                slug='{}_{}'.format(url,i),
                content='新闻详细内容： {} {}'.format(column_name, i),
            )[0]
            article.column.add(c)##文章和栏目的对应关系表


if __name__ == '__main__':
    main()
    print("Done!")
