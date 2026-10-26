FROM python:3.12-alpine

WORKDIR /app

RUN pip install --no-cache-dir pytest==8.4.2 requests==2.32.5

COPY test_api.py .

CMD ["pytest", "-v"]
