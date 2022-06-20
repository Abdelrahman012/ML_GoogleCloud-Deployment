FROM python:3.9-slim

COPY requirements.txt .
RUN pip install reuirements.txt

RUN mkdir -p app
COPY ./app app

EXPOSE  8080

CMD ["python", "./main.py", "--config=config.py"]
