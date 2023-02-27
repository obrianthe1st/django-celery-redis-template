# Django-Celery-Redis-Template v2.0

## Overview

I have done a complete overhaul of the first version of the first version of this repo as it was a bit messy and all over the place. I now instead decided to work on a new version for others to use. Now let's get to the meat of the matter.

## Main Tools Included

Nginx
Django
Postgres
Celery
Redis

## How to get started

`docker-compose -f local.yml up` -- to build and get the codebase up and running

`docker-compose -f local.yml run api sh -c "python manage.py runserver" ` -- I use this to execute various django commands on a separate terminal in vscode while I have the main docker terminal up and running to view the logs. There are many different ways to get the same result in docker.`

### requirements/

The requirements folder contain the requirements for our project. It starts from base.txt which contains the base requirements for our project. local.txt and production.txt contains the requirements for production and local environment respectively.

### core/

The core directory is the main directory for the project with the default setup the django project.

### core/settings/

Inside this directory you will find three different settings.py file:

1. base.py
   The base.py file will contain the main boilerplate settings for the project.
2. local.py
   The local.py file will contain the local settings for the project for your local environment.
3. production.py
   The production.py file will contain the production settings for the project for your production environment.

### core_apps/

This directory contains all the apps for our projects. If you check the base settings file you will see that the settings for the apps layout is a bit different.

## Nginx as reverse proxy

I use nginx as a reverse proxy for our application. Instead of sending the request directly to the python backend, it will instead go to the proxy address,`localhost:8080`, nginx will do its magic and send the request to the default django server `localhost:8000`.

To access a url in django you would have to now use the nginx address along with the rest of the url.

To be able to make changes to nginx you can do easily inside the directory path: docker/local/nginx/default.conf.

I decided to change the admin path to `localhost:8080/secretadmin`. It is for security purposes you can easily change it in base settings with `ADMIN_URL=`. An example is provided in the settings file anyway.

### .envs/.local/

Inside this folder you will store the environment variables inside the various different files provided. You can create your own files as well and add your own touch to it.

### docker/

All the docker files are now in one place. If you dig into the local folder you will notice there are various settings for django, celery, nginx and postgres.

I got bash scripts setup inside to handle some of the automation parts of it. You can dig into that as well.
