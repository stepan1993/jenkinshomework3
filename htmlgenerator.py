html = "Hello world"

def check_user_name(name):
	return name=="Stepan"

with open('index.html', 'w') as f:
    f.write(html)
