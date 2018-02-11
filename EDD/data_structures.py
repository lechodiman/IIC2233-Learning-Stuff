# Queue: special type of lists
queue = ["wake up", "have a coffee", "have a shower", "get dressed", "have breakfast",
         "go to work"]


class queue_class:

    def __init__(self, queue):
        self.queue = queue

    def view():
        for x in range(leng(self.queue)):
            print(self.queue[x])

    def push():
        item = input("please enter the item you wish to add")
        self.queue.append(item)

    def pop():
        item = self.queue.pop(0)
        print("you popped out : ", item)

# stacks: data is pushed and retrieved from the same end

#from collections import deque
#
#cola = deque()
#
# cola.append('naranja')
# cola.append('manzana')
# cola.append('platano')
#
#d = deque()
#d.extend(['r','a', 'd', 'a', 'r', 'e', 's'])
# print(d)
# print(len(d))
#
#print(d[0], d[-1])
#
# d.rotate(3)
# print(d)
#
#primero = d.popleft()
#ultimo = d.pop()
#
#print(primero, ultimo)
# print(d)

lista_canciones = [("Uptown Funk", "Mark Ronson"),
                   ("Thinking Out Loud", "Amy Wadge "),
                   ("Sugar", "Maroon 5"),
                   ("Patterns In The Ivy", "Opeth"),
                   ("Take Me To Church", "Hozier"),
                   ("Style", "Taylor Swift"),
                   ("Love Me Like You Do", "Ellie Goulding")]
artistas = set()
for cancion, artista in lista_canciones:
    artistas.add(artista)


mis_artistas = {'Hozier', 'Opeth',
                'Ellie Goulding', 'Mark Ronson', 'Taylor Swift'}
artistas_album = {'Maroon 5', 'Taylor Swift', 'Amy Wadge'}

#print("Todos: {}".format(mis_artistas.union(artistas_album)))
#print("Ambos: {}".format(artistas_album.intersection(mis_artistas)))
#print("Cualquiera pero no ambos: {}".format(artistas_album.symmetric_difference(mis_artistas)))

mis_artistas = {'Opeth', 'Ellie Goulding', 'Mark Ronson', 'Taylor Swift'}
bandas = {"Opeth", "Guns N' Roses"}

print("issuperset: {}".format(mis_artistas.issuperset(bandas)))

mis_numeros = {i for i in range(10)}
mis_pares = {i for i in range(0, 10, 2)}
mis_pares.difference({2, 4})
print(mis_pares)
# print(mis_pares.issubset(mis_numeros))
