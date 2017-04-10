Still not too sure how to do the spark stuff, kafka seems straightforward though.


Required:
Docker with Docker-Compose
Check if compose is installed with: docker-compose -version

Usage(I sudo infront of all my commands):

Startup these 5 containers (2 spark, 1 zookeeper, 1 kafka, 1 tweepy) by going into this directory and typing:
sudo docker-compose up

See active containers in different terminal(any directory):
sudo docker ps

Kill all containers:
sudo docker kill $(sudo docker ps -q)


