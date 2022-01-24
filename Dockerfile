FROM python:3.8.1-slim-buster
#RUN apt-get update && \
#    apt-get -y install gcc && \
#    rm -rf /var/lib/apt/lists/*
#RUN apt-get update \
#&& apt-get install gcc -y \
#&& apt-get clean
RUN mkdir -p projects/
RUN pip install virtualenv
WORKDIR projects
RUN virtualenv -p python3.8 env
#ENV PATH="/projects/env/bin:$PATH"
COPY requirements.txt .
# RUN /bin/bash -c "echo $pwd"
RUN /bin/bash -c "source env/bin/activate && pip install -r requirements.txt"
# RUN source env/bin/activate
# RUN pip install -r requirements.txt
RUN mkdir "django_app"
COPY . django_app/
WORKDIR django_app
#ENTRYPOINT ["python", "manage.py", "runserver"]
