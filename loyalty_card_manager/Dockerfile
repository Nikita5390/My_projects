FROM python:3.10

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:5000"]

EXPOSE 8000/tcp