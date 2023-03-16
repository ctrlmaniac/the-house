FROM python:3.11-alpine3.16

COPY thehouse /thehouse

CMD ["python", "-m", "thehouse"]