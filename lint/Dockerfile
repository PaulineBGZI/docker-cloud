FROM python:3.12-alpine

WORKDIR /app

RUN pip install --no-cache-dir ruff==0.14.2

ENTRYPOINT ["ruff", "check", "--no-cache"]
CMD ["."]
