from django import template
 
register = template.Library()

from django import template

register = template.Library()


@register.filter(name='censor')
def censor(val, arg):
    banned_words = ['ниггер', 'жид','идиот', 'дрянь', 'придурок', 'дерьмо', 'черт', 'козел']
    text = val
    result = ''

    for word in banned_words:
        data = text.lower().replace(word, arg * len(word))
        text = data

    for i in range(len(val)):
        if val[i] != text[i]:
            result += text[i].upper()
        else:
            result += text[i]

    return result