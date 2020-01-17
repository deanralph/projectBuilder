FROM alpine

RUN apk add python3-dev

RUN pip3 install flask

COPY . /app/

EXPOSE 5000

CMD "python3 /app/main.py"