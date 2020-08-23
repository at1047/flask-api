sudo docker stop booking 
sudo docker rm booking 
sudo docker run -p 5432:5432 -e POSTGRES_USER=appseed -e POSTGRES_PASSWORD=appseed -d --name db postgres
sudo docker build -t cph1c06/booking .
sudo docker run -d --link db --name booking -p 5000:5000 cph1c06/booking

