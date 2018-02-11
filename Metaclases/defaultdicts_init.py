from collections import defaultdict

results = defaultdict(lambda: 1, {'Chile': 2, 'Colombia': 0})
print(results['Chile'])
print(results['Argentina'])
print(results['USA'])
print(results['Paraguay'])
del results['Colombia']
print(*results.keys(), sep='\n')
