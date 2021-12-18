def  check_user_name(name):
	return name=="Stepan"


html_template = """
<html>
<head></head>
<body>
<p>Does your name is Stepan? </p>
<p>
"""
if check_user_name("Stepan"):
	html_template+="Yes, my name is Stepan"
else:
	html_template="No, I'm not Stepan"
html_template+="""  
</p>
</body>
</html>
"""
with open("index.html","w") as file:
	file.write(html_template)
