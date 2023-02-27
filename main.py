'''
Створити власний декоратор, який в якості аргументів прийматиме об’єкти типу int або str
і в залежності від отриманого типу- буде при виконанні функції передавати функції кортеж,
в якому буде міститися словник, парами якого будуть: тип елементу / елемент.
Функціонал самої функції- не важливий.
'''


def decorator(*i):
    def main_func(func):
        def wrapper(*args, **kwargs):
            return func(*i, *args, **kwargs)
        return wrapper
    return main_func
@decorator(4, 'b')
def func_for_deco(*args):
    type_i = [type(j) for j in args]
    for j in args:
        dct = {key: value for key, value in zip(type_i, args)}
    return dct
n = func_for_deco()
print(n)

