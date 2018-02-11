'''
file = open('archivo_ejemplo', 'r', encoding='ascii', errors='replace')
print(file.read())
file.close()

contenido = 'sorry pero ahora yo soy lo que habrá dentro del archivo'
file = open('archivo_ejemplo', 'w', encoding='ascii', errors='replace')
file.write(contenido)
file.close()
'''

# bytesarays

b = bytearray(b'abcdef')


contenido = b'abcde12'
file = open('archivo_ejemplo_2', 'rb')
print(file.read())
file.close()

num_lineas = 100
file = open('archivo_ejemplo_3', 'wb')
for i in range(num_lineas):
    contenido = b'linea_' + bytes([i]) + b'abcde12'
    file.write(contenido)
file.close()

file = open('archivo_ejemplo_3', 'rb')
print(file.read(41))
file.close()
