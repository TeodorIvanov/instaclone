import re

from .models import Tag


def get_hashtags_from_description(instance):
    tags = re.findall(r"#(\w+)", instance.description)
    pic_tags = []
    for title in tags:
        pic_tag, created = Tag.objects.get_or_create(title=title)
        pic_tags.append(pic_tag.pk)
    return pic_tags
