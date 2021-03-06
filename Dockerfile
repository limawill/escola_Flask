FROM python:3.7-alpine
LABEL maintainer="Will Lima <limawill83@gmail.com>"
WORKDIR /app
ENV FLASK_ENV=development
ENV FLASK_APP=app:create_app
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
