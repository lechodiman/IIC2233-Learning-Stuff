
site_title = "My Blog"
'''
def blog_posts(title, *args):
	print(title)
	for arg in args:
		print(arg)
'''

def blog_posts(title,*args, **kwargs):
	print(title)
	for arg in args:
		print(arg)
	for p_title, post in kwargs.items():
		print(p_title, post)
'''
blog_posts(site_title,
		"1","2","3", 
		blog_1 = "I am so awesome", 
		blog_2 = "Cars are so cool", 
		blog_3 = "Aww look at my cat!")
'''

def graph_operation(x, y):
	print("function that graphs {} and {}".format(str(x), str(y)))

x1 = [1,2,3]
y1 = [2,3,1]

graph_operation(x1, y1)
