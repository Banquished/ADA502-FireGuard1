# Use Node.js Alpine base image
FROM node:18-alpine

# Create and set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json /app/

# Install dependencies
RUN npm install

# Copy the entire codebase to the working directory
COPY . .

# Expose the port your app runs on
EXPOSE 3000

# Define the command to start your application
CMD ["npm", "start"]


# Commands to build and run the Docker image
# docker build -t frontend .
# docker run -p 3000:3000 -d frontend

# Docker Compose uses a while to boot up frontend currently
# The server might be accessible at http://172.18.0.3:3000/ earlier.
# Command for running frontend and backend as docker-compose is:
# docker-compose up --build