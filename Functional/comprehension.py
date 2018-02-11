nums = [1,2,3,4,5,6,7,8,9, 10]

my_list = [n for n in nums if n % 2 == 0]
#print(my_list)

my_list_2 = [(letter, num) for letter in 'abcd' for num in range(4)]

#print(my_list_2)

names = ["Bruce", "Clark", "Peter"]
heros = ["Batman", "Superman", "Spiderman"]

zipped = zip(names, heros)
#print(list(zipped))

dict_names_heros = {name: hero for (name, hero) in zipped if name != 'Peter'}
#print(dict_names_heros)

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]

my_set = {n for n in nums}
print(my_set)