FROM python:3.10.6-alpine

WORKDIR /thehouse

COPY thehouse /thehouse

CMD ["python", "-m", "thehouse"]