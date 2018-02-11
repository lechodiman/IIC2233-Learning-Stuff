try:
	f = open("usuarios.csv")
	if f.name == 'usuarios.csv':
		raise Exception
except Exception:
	print("This file is bad")
finally:
	f.close()