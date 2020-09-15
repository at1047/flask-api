sudo docker stop todo-api 
sudo docker rm todo-api 
sudo docker run -p 5432:5432 -e POSTGRES_USER=appseed -e POSTGRES_PASSWORD=appseed -d --name db postgres
sudo docker build -t at1047/todo-api .
sudo docker run -d --link db --name todo-api -p 5000:5000 at1047/todo-api

