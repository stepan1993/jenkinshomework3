FROM nginx
RUN apt update && apt -y install python3

WORKDIR /app
COPY . . 
<<<<<<< HEAD
RUN python3 -m unittest check_name.py
=======
RUN python3 -m unittest test_name.py
>>>>>>> 2a387e629dbd5655e5888dc61660900be9449c29
RUN python3 htmlgenerator.py
RUN mv index.html /usr/share/nginx/html
