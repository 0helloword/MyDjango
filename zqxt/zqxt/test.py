import random

article_title_list = ['Django 教程', 'Python 教程', 'HTML 教程']
for article_title in article_title_list:
        # 从文章标题中得到 tag
    tag_name = article_title.split(' ', 1)[0]
#     tag, created = Tag.objects.get_or_create(name=tag_name)
 
    print(tag_name)
