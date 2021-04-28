# Getting started

This guide outlines how to set up a new URLP deployment. The supported deployment option is through provided docker-compose files using a SQLite3 database as persistence which should
work fine for most scenarios.

## Prerequisites

* CentOS
* Docker 
* docker-compose

## Basic Setup

1. Download the standalone docker-compose config from the [releases](https://github.com/splunk/urlprompt/releases) page.
2. Extract the archive on the deployment host
3. Switch into the extracted directory
4. Run the stack

```
docker-compose up
```

## Setup with self-signed HTTPS

The proxy docker-compose configuration additionally deploys an nginx container as a reverse proxy to terminate TLS connection. By default, the bundle contains an insecure,
self-signed key. It is strongly recommended to either deploy a trusted cert or [generate your own](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-on-debian-8). 

1. Download the proxy docker-compose config from the [releases](https://github.com/splunk/urlprompt/releases) page.
2. Extract the archive on the deployment host
3. Switch into the extracted directory
4. Run the stack

```
docker-compose up
```
