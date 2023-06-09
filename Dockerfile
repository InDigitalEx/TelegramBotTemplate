# syntax=docker/dockerfile:1

FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "run.py"]
