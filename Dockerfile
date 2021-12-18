FROM nginx
RUN apt update && apt -y install python3

WORKDIR /app
COPY . . 
RUN python3 -m unittest check_name.py
RUN python3 htmlgenerator.py
RUN mv index.html /usr/share/nginx/html
