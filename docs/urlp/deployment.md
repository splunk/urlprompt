# Deployment

This guide outlines how to set up a new URLP deployment.

## Prerequisites

* docker 
* docker-compose

## Basic Setup

Download the docker-compose.yml on the deployment host:
```
curl https://github.com/splunk/urlprompt/releases/download/edge/docker-compose.yml --output docker-compose.yml
```

Create the database folder which will persist the database:
```
mkdir db
```

Run the stack: 
```
docker-compose up
```
