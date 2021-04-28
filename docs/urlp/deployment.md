# Deployment

This guide outlines how to set up a new URLP deployment.

## Prerequisites

* docker & docker-compose

## Docker

To get a basic instance up and running, execute the following command

```
docker run -e SECRET_KEY=changeme -e DATABASE_URL=sqlite:////db/db.sqlite3 -v <absolute-path-to-db-folder>:/db -p 5000:5000 ghcr.io/splunk/urlprompt:latest
```

## Docker Compose

Alternatively, you can use [docker-compose](https://docs.docker.com/compose/) to get a more advanced deployment with an Nginx reverse proxy to provide HTTPS.


## Configuration


## HTTPS

