FROM python:3.8.10-alpine3.14
COPY . .
RUN apk update && apk add python3-dev \
                      gcc \
                      libc-dev \
                      libffi-dev 
RUN pip install -r requirements.txt -U --pre
CMD ["python", "app.py"]
