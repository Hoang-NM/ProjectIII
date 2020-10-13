def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


for x in (-1, 0, 1):
    print(sign(x))


def hello(name: str, loud=False):
    if loud:
        print('Hello %s!' % name.upper())
    else:
        print('Hello %s!' % name)


hello('Hoang')
hello('Hong', loud=True)
