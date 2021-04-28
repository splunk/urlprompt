# Deployment

This guide outlines how to set up a new URLP deployment.

## Prerequisites

* docker 
* docker-compose

## Basic Setup

1. Download the docker-compose config from the [releases](https://github.com/splunk/urlprompt/releases) page.
2. Extract the archive on the deployment host
3. Switch into the extracted directory
4. Run the stack

```
docker-compose up
```