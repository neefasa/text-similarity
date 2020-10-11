# Measuring the similarity between two texts

I used [this notebook](testing/test-text-sim.ipynb) to develop an MVP model. I went with cosine similarity of word counts.

---
## Run as a Python Script
The python script can be run on the command line. It takes in a json file with the text samples.

```
$ python text_similarity.py <file.json>
```
If you are in the root of this repository, you can run the following line.
```
$ python app/text_similarity.py samples.json
```
The output would be:
```
Sample1 and Sample2 have a similarity of 0.89
Sample1 and Sample3 have a similarity of 0.56
Sample2 and Sample3 have a similarity of 0.58
```
---
## Deployed on Heroku with a simple user interface  
I deployed the app using Flask, Heroku, and Docker. It has a simple interface, and can also take post requests.  


[text-sim.herokuapp.com](https://text-sim.herokuapp.com)  

![text sim app](images/text-sim-app.png)  

## Access the app using a post request

![api test](images/api-text-img.png "API test using some text in a json")


---
## Build the Docker container
If you don't already have Docker CLI, download it [here](https://www.docker.com/get-started).

To create the Docker container, navigate to the app folder of this repo and run the following command:
```
$ docker build -t <any tag> .
```
`<any tag>`  can be anything. It's a tag to easily reference the container. For example the above command would look like this if I chose text-sim as the tag.
```
$ docker build -t text-sim .
``` 

## The Docker container through Dockerhub
I have a container on Dockerhub that can be pulled with the following command. In this case the container tag would be neefasa/text-similarity.
```
$ docker pull neefasa/text-similarity
```

## Run the container
Now the container should be run, using the appropriate tag. If you pulled the container, use the following command:
```
$ docker run -dp 5000:5000 neefasa/text-similarity
```
Now the app should be running in a local server. To access it, open [localhost:5000](http://localhost:5000) in a browser.

## Stop the container
Make sure to stop the server when you are done with it. In order to do that, first you will have to find the container id. Find that with this command:
```
$ docker ps
```
Find the container id for the container that you want to stop.
```
$ docker stop <container id>
```
Then you will want to remove it. 
```
$ docker rm <container id>
```

