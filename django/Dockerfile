FROM python

ENV PYTHONUNBUFFERED 1

# db
ENV DB_ENGINE django.db.backends.postgresql
ENV DB_NAME postgres
ENV DB_USER postgres
ENV DB_PASSWORD postgres
ENV DB_HOST ModelSite-db
ENV DB_PORT 5432

# broker
ENV BROKER_USER admin
ENV BROKER_PWD *p4ss_3ntelMS
ENV BROKER_ADDRESS 10.30.7.70


RUN mkdir ModelSite_Project
WORKDIR ./ModelSite_Project

COPY ./ModelSite_Project .
COPY requirements.txt .

RUN pip install -r requirements.txt

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]