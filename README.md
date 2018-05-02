# Docker
The python and JSON file must be present in the same folder.

Create the Dockerfile edit it to contain in it all the commands you want to execute.

Create Docker Image: docker build -t flask-image:latest .

Run the app image inside a container: docker run -d -p 5000:5000 --name flask-container flask-image

To check list of running docker containers: docker ps 

Go to the browser and enter: http://192.168.99.100:5000/music
