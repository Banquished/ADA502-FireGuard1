<span style="color:red">FireGuard 🔥</span>
=========

## Introduction
The FireGuard project is part of ADA502 Cloud Computing and Software Systems, a master course at Western Norway University of Applied Sciences. The course covers software technologies that can be used to develop systems employing a combination of web application frontends, cloud-based compute-, communication- and data-storage services, and IoT devices.

The project is undertaken by the following students:

⭐ Ole-Marius O. Ask

⭐ Kim André N. Trengereid

⭐ Sivert H. Benjaminsen

⭐ Halldor Broddi Thorsteinsson

Utilizing API calls to acquire weather data from the Norwegian Meteorological Institute (MET), the group has developed backend and frontend applications to predict and display the fire risk in the form of time-to-flashover values at user-specified locations within Norway.  

------------------

# <span style="color:orange"> Prerequisites </span>
* [Node.js](https://nodejs.org/en/download/) - is an open-source, cross-platform JavaScript runtime environment allowing developers to execute JavaScript code outside a web browser. It is commonly used to build scalable network applications like web servers and APIs.
* [Python 3.11](https://www.python.org/downloads/) - is a computer programming language often used to build websites and software, automate tasks, and analyze data. [Poetry](https://python-poetry.org/docs/#installation) is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on, and it will manage (install/update) them for you.
* [Docker](https://docs.docker.com/get-docker/) - is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime.

## Contribution & Credits
This course project extends the research presented in the paper by Strand and L.M. Larsen titled “An Implementation, Evaluation, and Validation of a Dynamic Fire and Conflagration Risk Indicator for Wooden Homes.”

The following repository contains the implementation of the dynamic fire risk indicator described in the submitted paper: [GitHub](https://github.com/selabhvl/dynamic-frcm)

## Getting Started
This section provides a detailed guide on how to successfully install the FireRisk project, covering each step from initial setup to final configuration to ensure a smooth and efficient installation process.

**Before beginning, ensure that you have downloaded the software mentioned in the Prerequisites section.**

This project can be installed locally using one of two methods described below. The recommended method is:

🔶 __Using DockerHub to run locally (reccomended)__

Alternatively, you can opt for:

🔷 __A full local installation__

For the first option, [Docker Desktop](https://www.docker.com/products/docker-desktop/) must be installed, and started on your computer.

## <span style="color:tomato">Method 1 - Installation using premade Docker Images via DockerHub</span>

This section guides you through pulling the docker images from DockerHub and running the images locally to boot up the application on localhost.

### <span style="color:orange">Step 1: Getting the images from DockerHub</span>
1. Make sure to have opened [Docker Desktop](https://www.docker.com/products/docker-desktop/) on your computer (It has to be running in the background)
2. Open a local terminal window (i.e. cmd / PowerShell)
3. Run `docker pull banquished/fireguardproject-backend` to pull the backend image
![image](https://github.com/Banquished/ADA502-FireGuard1/assets/105752308/4c4058a5-eae3-424a-82c9-f68df554bcd5)

4. Run `docker pull banquished/fireguardproject-frontend` to pull the frontend image
![image](https://github.com/Banquished/ADA502-FireGuard1/assets/105752308/56a2a2c7-94b7-4faa-bde7-13bdad526851)

5. Run `docker images` to show all the existing docker images on your local machine.
![image](https://github.com/Banquished/ADA502-FireGuard1/assets/105752308/da213505-ea3c-41e9-928f-ac979dcda8fe)

6. Open the Docker Dekstop Application - You should now see the images in the images folder.
![image](https://github.com/Banquished/ADA502-FireGuard1/assets/105752308/445212b0-5c4b-4a5c-9672-051db9e4114e)

7. Manually run the backend image ( `banquished/fireguardproject-backend` ) and choose the host port 8000
![image](https://github.com/Banquished/ADA502-FireGuard1/assets/105752308/d14ae8de-433d-4c80-ad7e-6585819dd292)

8. Manually run the frontend image ( `banquished/fireguardproject-frontend` ) and choose the host port 3000
![image](https://github.com/Banquished/ADA502-FireGuard1/assets/105752308/7295cefa-dac9-470a-9204-56cb4780a60b)

9. Navigate to the Containers folder to see both frontend and backend running within the same compose-stack.
![image](https://github.com/Banquished/ADA502-FireGuard1/assets/105752308/44845095-93f0-42a7-9c55-6c00425d0210)

10. You should now be able to open up backend on [localhost:8000](http://localhost:8000/apicall) and frontend on [localhost:3000](http://localhost:3000) respectively.

Congratulations, that's it! Everything should be up and running.


## <span style="color:tomato">Method 2: Local Installation</span>
Before starting step 1, make sure to have downloaded the prerequisites mentioned in the start of this file.

### <span style="color:orange">Step 1: Cloning the Repository</span>
1. Go to the [GitHub page](https://github.com/Banquished/ADA502-FireGuard1) for this repository.
2. Click the "Code" button, copy the URL under "Clone with HTTPS".
3. Open a terminal on your local machine, navigate to the directory where you want to clone the repository.
4. Run `git clone https://github.com/Banquished/ADA502-FireGuard1.git`
5. `cd ADA502-FireGuard1`
6. Open VS-code via `code .`

### <span style="color:orange">Step 2: Installing & Running the project locally</span>
All of the commands below will assume a starting point from the root directory.

In order to connect the backend and the frontend locally, one has to make sure that both frontend and backend is running simultaneously.

#### <span style="color:orange">Step 2.1: Frontend</span>

```
cd .\frontend\
npm install
npm start
```

-----------------
#### <span style="color:orange">Step 2.2: Backend</span>
```
cd .\FRCM-app\
poetry install
python manage.py runserver 0.0.0.0:8000
```
-----------------

### <span style="color:orange">Step 3: Creating and running Docker Images using Docker Run or Docker-Compose</span>

#### <span style="color:orange">Step 3.1: With Docker-Compose</span>
From the root directory, simply run the following command:

`docker-compose up`

❗When running `docker-compose up`, the frontend application needs around 10-15 minutes to boot properly. This is due to frontend running as a development server, instead of being built as a production server❗

That's it! 

The frontend app should now be visible at [localhost:3000](http://localhost:3000), and the backend app should be visible at [localhost:8000](http://localhost:8000).


#### <span style="color:orange">Step 3.2.1: With Docker Run - Backend</span>
To build and run the Docker image for the Django backend, use the following commands (This assumes you are in the project directory root):
```
cd ./FRCM-app/
docker build -t backend .
docker run -p 8000:8000 -d backend
```
Your backend app should now be visible at [localhost:8000](http://localhost:8000) and [127.0.0.1:8000](http://127.0.0.1:8000).

##### <span style="color:orange">Step 3.2.2: With Docker Run - Frontend</span>
To build and run the Docker image for the React frontend, use the following commands (This assumes you are in the project directory root):
```
cd ./frontend/
docker build -t frontend .
docker run -p 3000:3000 -d frontend
```

Your frontend app should now be visible at [localhost:3000](https://localhost:3000) and [127.0.0.1:3000](https://127.0.0.1:3000).
