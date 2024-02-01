'''
Functii
o functie in python este un bloc de cod care este proiectat pentru a aexecuta o anumita sarcina.Functia se defineste o singura data  iar apoi poate fi apelata de mai multe ori in orice program,permitind reutulizarea codului
funtiile ajuta la organizarea si structuraraea codului si pot primii date de intrare(numite argumete)si pot returna date de iesire(prin intermnediul valorii returnate

'''


def my_function():  # signatura functiei (contine numele eie si orice poate aparea in paranteze)
    # in interiorul functiei vom scrie corpul functiei
    print('Hello din functie!')


my_function()  # apelare prin adaugare paranteze(daca nu punem paranteze nu se apeleaza)


# functii cu parametrii
def say_hy(name):
    print(f'Hy {name} .')


say_hy('Istvan')


# functii cu doi parametrii
def arata_suma(a, b):
    print(a + b)


arata_suma(3, 7)
arata_suma(2, 7)
arata_suma(1, 7)


# afisarea cheilor dintr-un dictionar
def arata_chei(dct):
    print(dct.keys())
    print(dct.values())


arata_chei({"a": 1, "b": 2})


# return intro functie python este folosit pentru a specifica ce valoare va fi trimisa inapoi la codul care a apelat functia
# este ca si cum ai spune dupa ce am terminat tot ce trebuie sa fac in functie voi da inapoi aceasta valoare
# acest lucru ajuta la transferul de informatii intre diferite parti al unui program si face ca functiile sa fie mai utile deoarece pot da un rezultat car il pot folosi in alte locuri in codul tau
def say_hello():
    return 'hello'  # functia se opreste din executie si se va intoarce in locul in care a fost apelata dand inapoi valorea hello


text = say_hello()
print(text)
print(say_hello())


def say_Hi():
    print(f'Hi')


text = say_Hi()
print(text)
print(30 * '.... ')


# functii cu parametri si return
def produs(a, b):
    return a * b


p = produs(2, 3)
print(p)


def is_even(number):
    # if number % 2 == 0:
    #  return True
    # return False
    return number % 2 == 0


def get_all_even_numbers(numbers):
    result = []
    for elem in numbers:
        # if elem % 2 == 0:
        if is_even(elem):
            result.append(elem)
    return result


nr = get_all_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(nr)
# tipuri de parametrii
def plus(a, b):  # a si b sunt parametrii (numele folosite pentru argumentele unui functii)
    return (a + b)


plus(1, 2)  # sunt argumente (argumentele sun valorile parametrilor)


# default arguments (parametrii cu valori implicite)
def plus(a, b=2):
    return (a + b)


plus(1)  # daca nu specificam o valoare explicita pentru b atunci va lua valoarea imlicita 2
plus(1, 3)  # daca ii dam o alta valoare atunci va ignora valoarea doi din functie
# keyword arguments
def plus(a, b):
    return (a + b)


plus(a=1, b=2)
plus(b=2, a=1)  # specificand argumentele pe numele lor nu este necesr sa pastram ordinaea


# nr valori pe parametri
def plus(*args):  # args este o conventie conteaza *
    print(args)
    return sum(args)


plus(1, 2, 3)
plus(*[1, 2, 3])  # steluta se numeste an paching scoate elemente dintro colectie


# keywords arguments
def plus(**kwargs):  # este un dictionar care contine toate argumentele date functiei
    print(kwargs)
    suma = sum(kwargs.values())
    print(f'suma este : ', suma)
    return suma


plus(a=1, b=2)


# plus(*1,2,3)


def exemple(*args, **kwargs):
    print(f'args: ', args)
    print(f'args', kwargs)
    suma_args = sum(args)
    print(f'suma_args', suma_args)

    suma_kwargs = len(kwargs)
    print(f'suma_kargs', suma_kwargs)


# exemple(*1, 2, 3, a=4, b=5, *[4, 5, 6])

