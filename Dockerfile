FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app 
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 5000
ENV POSTGRES_USER=appseed
ENV POSTGRES_PASSWORD=appseed
ENV POSTGRES_DB=appseed
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
ENTRYPOINT ["python3", "app.py"] 
