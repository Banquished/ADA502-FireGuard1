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

To install this project __locally__, one first has to fork the repository from GitHub. Then, make sure you have the following prerequisites as shown below.

### Prerequisites
* [Node.js](https://nodejs.org/en/download/)
* [Python 3.9](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org/docs/#installation)
* [Docker](https://docs.docker.com/get-docker/)

### Forking and Cloning the Repository
1. Go to the [GitHub page](https://github.com/Banquished/ADA502-FireGuard1) for this repository.
2. Click the "Fork" button at the top right of the page.
3. Once the repository is forked, you will be taken to your copy of the repository on your GitHub account.
4. Click the "Code" button, copy the URL under "Clone with HTTPS".
5. Open a terminal on your local machine, navigate to the directory where you want to clone the repository.
6. Run `git clone URL_OF_FORKED_REPO`, replacing `URL_OF_FORKED_REPO` with the URL you copied in step 4.


### Installing & Running the project locally
All of the commands below will assume a starting point from the root directory.

In order to connect the backend and the frontend locally, one has to make sure that both frontend and backend is running simultaneously.

#### Frontend

```
cd .\frontend\
npm install
npm start 3000
```

-----------------
#### Backend
```
cd .\FRCM-app\
poetry install
python manage.py runserver 8000
```
-----------------

Docker Images
--------------

#### Backend
To build and run the Docker image for the Django backend, use the following commands (This assumes you are in the project directory root):
```
cd ./FRCM-app/
docker build -t backend .
docker run -p 8000:8000 -d backend
```
Your backend app should now be visible at [localhost:8000](localhost:8000) and [127.0.0.1:8000](127.0.0.1:8000).

#### Frontend
To build and run the Docker image for the React frontend, use the following commands (This assumes you are in the project directory root):
```
cd ./frontend/
docker build -t frontend .
docker run -p 3000:3000 -d frontend
```

Your frontend app should now be visible at [localhost:3000](localhost:3000) and [127.0.0.1:3000](127.0.0.1:3000).
