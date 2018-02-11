import json


def foo(d):

    if '__class__' in d:
        nombre = d.pop('__class__')
        inst = type(nombre, (), d)

    else:
        inst = d

    return inst


# JSON message
msg1 = '{"g1": 1, "__class__": "F", "g2": 20}'
msg2 = '{"g1": 15, "g2": 200}'

a = json.loads(msg1, object_hook=foo)
b = json.loads(msg2, object_hook=foo)

print(a)
print(b)
