# Runbook

Useful commands to administer a running URLP deployment


## Create shell inside container

```
docker exec -it <docker-container-id> /bin/bash
source /venv/bin/activate
```


## Create new API user + token
```
python manage.py createapitoken <new-user>
```


## Reset superuser password
```
python manage.py changepassword <superuser>
```