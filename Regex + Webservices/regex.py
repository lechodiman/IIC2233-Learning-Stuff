import re

# Definamos un conjunto de secuencias que necesitamos verificar cumplen con
# un determinado patrón.
seq = ["4tt", "4ttabcabc32", "3ssafjabc33", "4tssssghj33", "4ttabcdag60", "4ttabcfgh41", "3ttabc4tt"]

# print(re.match('^(4tt)', seq[0]))
# print(re.match('^(4tt)', seq[4]))
# print(re.match('^(4tt)', seq[-1]))

for s in seq:
    # Indicaremos con los '{ }' el número de veces que el grupo debe estar presente.
    # Como vemos, por defecto se asume que puede estar 1 o más veces.
    if re.match('^4tt(abc){2}', s):
        print("{} cumple con el patron".format(s))


def is_valid_mail(email):
    pattern = '[a-zA-Z0-9_.]+@((seccion1|seccion2)\.)?(mail|mimail).cl'

    return bool(re.match(pattern, email))


def is_valid_rut(rut):
    pattern = '[0-9]{1,2}\.?[0-9]{1,3}\.[0-9]{3}-([0-9]|k|K)'
    pattern = '\d{1,2}\.?\d{1,3}\.\d{1,3}-(\d|k|K)'

    return bool(re.match(pattern, rut))


# print(is_valid_mail('nombre.apellido@seccion1.mail.cl'))
# print(is_valid_rut('12.224.877-1'))
seq = ["4tt", "4ttabcabc32", "3ssafjabc33", "4tssssghj33", "4ttabcdag60", "4ttabcfgh41", "3ttabc4tt"]

# for s in seq:
#     print('secuencia {}: {}'.format(s, re.findall('(ab)', s)))

# for s in seq:
#     print('secuencia {}: {}'.format(s, re.findall('\d+', s)))

for s in seq:
    # sub retorna un nuevo valor, por lo tanto, no modifica la secuencia original
    print('Secuencia {} queda como {}'.format(s, re.sub('\d+', '', s)))
