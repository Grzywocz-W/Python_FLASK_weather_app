
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y postgresql-client && pip install -r requirements.txt

COPY app/ .

RUN chmod +x wait-for-postgres.sh

CMD ["./wait-for-postgres.sh"]
