FROM python:3.10.6-alpine

COPY thehouse /thehouse

CMD ["python", "-m", "thehouse"]