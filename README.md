# Test task for BEST Hackath0n
> Team name: based

This repository contains all of the source code for our web app.

## Web App
The app itself is hosted on Heroku. You can access it [here](https://based-app.pp.ua/).

## API Documentation
You can find the documentation for our app's API [here](https://www.based-app.pp.ua/api/docs/).

## Stack
Needz was built using React + Django, backend uses SQLite as database, but it's easily replaceable. It uses specific deploy config, written primarily for Heroku to enable continuous CI/CD. App deploys on push to the main branch of this repo.

## How to deploy locally
In order to deploy locally, you need to have Python 3.10.x and npm installed on your machine. To install dependencies and run it locally, you should clone this repo, then run init.sh, and run.sh consecutively. If you're on Windows, try rewriting these shell scripts so that they run on Windows :)