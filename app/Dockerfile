FROM python:3.6
LABEL maintainer "r-suyama <r-suyama@colorful-board.com>"
WORKDIR /usr/src/app
COPY app.py uwsgi.ini requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3031
CMD ["uwsgi", "uwsgi.ini"]
