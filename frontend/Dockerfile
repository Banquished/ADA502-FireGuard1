# Use Node.js Alpine base image
FROM node:alpine

# Create and set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json /app/

# Install dependencies
RUN npm install

# Copy the entire codebase to the working directory
COPY . /app/

# Expose the port your app runs on
EXPOSE 3000

# Define the command to start your application
CMD ["npm", "start"]


# Commands to build and run the Docker image
# docker build -t frontend .
# docker run -p 3000:3000 -d frontend