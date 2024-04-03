FireGuard
=========
The FireGuard Project is a part of the course ADA502, which takes place during the spring semester of 2024. 

Our group consists of the following members:
* __Ole-Marius O. Ask__
* __Kim André N. Trengereid__
* __Sivert H. Benjaminsen__
* __Halldor Broddi Thorsteinsson__


Installation
------------

To install this project __locally__, one first has to clone the repository from GitHub. Then, make sure you have the following prerequisites as shown below.

### Prerequisites
* [Node.js](https://nodejs.org/en/download/)
* [Python 3.11](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org/docs/#installation)
* [Docker](https://docs.docker.com/get-docker/)

### Cloning the Repository
1. Go to the [GitHub page](https://github.com/Banquished/ADA502-FireGuard1) for this repository.
2. Click the "Code" button, copy the URL under "Clone with HTTPS".
3. Open a terminal on your local machine, navigate to the directory where you want to clone the repository.
4. Run `git clone https://github.com/Banquished/ADA502-FireGuard1.git`
5. `cd ADA502-FireGuard1`
6. Open VS-code via `code .`


### Installing & Running the project locally
All of the commands below will assume a starting point from the root directory.

In order to connect the backend and the frontend locally, one has to make sure that both frontend and backend is running simultaneously.

#### Frontend

```
cd .\frontend\
npm install
npm start
```

-----------------
#### Backend
```
cd .\FRCM-app\
poetry install
python manage.py runserver 0.0.0.0:8000
```
-----------------

#### Creating and running Docker Images using Docker-Compose

##### Backend
To build and run the Docker image for the Django backend, use the following commands (This assumes you are in the project directory root):
```
cd ./FRCM-app/
docker build -t backend .
docker run -p 8000:8000 -d backend
```
Your backend app should now be visible at [localhost:8000](http://localhost:8000) and [127.0.0.1:8000](http://127.0.0.1:8000).

##### Frontend
To build and run the Docker image for the React frontend, use the following commands (This assumes you are in the project directory root):
```
cd ./frontend/
docker build -t frontend .
docker run -p 3000:3000 -d frontend
```

Your frontend app should now be visible at [localhost:3000](https://localhost:3000) and [127.0.0.1:3000](https://127.0.0.1:3000).

Installation using premade Docker Images via DockerHub
--------------

This section guides you through pulling the docker images from DockerHub, cloning the repository and running the images locally to boot up the application on localhost.

#### 1. Getting the images from DockerHub
We first have to run the following commands to get the images:

```
docker pull banquished/fireguardproject-backend
docker pull banquished/fireguardproject-frontend
```
Then, move on to the next step..

#### 2. Cloning the repository
The purpose behind cloning the repository is to run the compose-file so that you won't have to separately build the images.

1. Go to the [GitHub page](https://github.com/Banquished/ADA502-FireGuard1) for this repository.
2. Click the "Code" button, copy the URL under "Clone with HTTPS".
3. Open a terminal on your local machine, navigate to the directory where you want to clone the repository.
4. Run `git clone https://github.com/Banquished/ADA502-FireGuard1.git`
5. `cd ADA502-FireGuard1`
6. Open VS-code via `code .`


#### 3. Add neccesary .env files
The application needs to have two different .env-files, these have to be placed at the correct location.

##### Frontend

The .env file for the frontend-application has to be put in the frontend-folder. When standing in the project root, you can simply do:
`cd .\frontend\`

See the image below to make sure you add the .env-file at the correct place.
![image](https://github.com/Banquished/ADA502-FireGuard1/assets/105752308/21057cb7-5ce9-47d7-92f7-2add3faf82dc)

Inside of the .env-file, you need to set the following environment variables:
```
REACT_APP_API_KEY_GOOGLE_MAPS='<INSERT API_KEY HERE>'
REACT_APP_API_MAP_ID='<INSERT MAP_ID HERE>'
API_URL='http://localhost:8000'
```
Credentials for using the Google Maps API can be obtained via:

[https://developers.google.com/maps](https://developers.google.com/maps)

Make sure to check out the documentation and follow those steps to get started.

[Google Maps Docs](https://developers.google.com/maps/documentation)

-------------------------
##### Backend

The .env file for the backend-application has to be put in the _"weatherdata"_-folder. When standing in the project root, you can simply do:

`cd .\FRCM-app\frcmApp\src\frcm\weatherdata\`

See the image below to make sure you add the .env-file at the correct place.

![image](https://github.com/Banquished/ADA502-FireGuard1/assets/105752308/d1bd39a6-07d7-4d1b-af17-ef119920492e)

Inside of the .env-file, you need to set the following environment variables:

```
MET_CLIENT_ID='<INSERT CLIENT ID HERE>'
MET_CLIENT_SECRET='<INSERT CLIENT SECRET HERE>'
```

Credentials for using the MET APIs can be obtained via:

[https://frost.met.no/auth/requestCredentials.html](https://frost.met.no/auth/requestCredentials.html)

--------------------------

#### 4. Run the application using Docker.
From the root directory, simply run the following command:

`docker-compose up`

That's it! The frontend app should now be visible at [localhost:3000](http://localhost:3000), and the backend app should be visible at [localhost:8000](http://localhost:8000).

--------------------------
