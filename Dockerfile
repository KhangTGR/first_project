FROM python:3-alpine

WORKDIR /app

COPY ./config/requirements.txt requirements.txt

RUN apk update && apk add python3-dev
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
CMD gunicorn --bind 0.0.0.0:5000 main:app