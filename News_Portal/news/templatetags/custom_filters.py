"""
Данный файл нужен для того, чтобы создавать и регистрировать собственные фильтры.
"""
from django import template
# если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются
register = template.Library()

# Теперь каждый раз, когда мы захотим пользоваться нашими фильтрами,
# в шаблоне нужно будет прописывать следующий тег:
# {% load custom_filters %}.


# Фильтр "Цензор"
# регистрируем наш фильтр под именем censor, чтоб django понимал, что это именно фильтр, а не простая функция
@register.filter(name='censor')
# аргумент здесь это то значение, к которому надо применить фильтр,
def censor(value):
    # создаем список зацензуренных слов
    censor_list = ['мат']
    # форматируем полученный текст
    text = value.split()
    # в цикле проходимся по тексту
    for word in text:
        # и если слово в нижнем регистре входит в список зацензуренных слов
        if word.lower() in censor_list:
            # то меняем это слово на [CENSORED]
            value = value.replace(word, '[CENSORED]')
    return value


# !!!! фильтр для примера !!!!
@register.filter(name='multiply')  # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg):  # первый аргумент здесь это то значение, к которому надо применить фильтр,
                           # второй аргумент — это аргумент фильтра, т. е.
                           # примерно следующее будет в шаблоне value|multiply:arg
    if isinstance(value, str) and isinstance(arg, int):
        return str(value)*arg  # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}')