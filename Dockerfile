FROM python:3.9

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

RUN apt-get update -y && apt-get install -y python3-venv

CMD ["python", "app.py"]

