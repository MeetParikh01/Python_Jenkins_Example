FROM python:3.8.1-slim-buster
RUN mkdir -p projects/
WORKDIR projects
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir "django_app"
COPY . django_app/
WORKDIR django_app
