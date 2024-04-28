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
Why npm? We intended to have both frontend and backend in here, but it happened that we have our backend and frontend as separate apps.

## Design for the app
Design for this app is located [here](https://www.figma.com/file/zQovKdtikLEx1MaZVli1kc/Hackath0n?type=design&node-id=0%3A1&mode=design&t=6naB5SNPHdY5DprS-1)  