
# Trackerrr - simple, but fully functional time tracking app


## Table of contents

- [General info](#general-info)
- [Live demo](#live-demo)
- [Screenshots](#screenshots)   
- [Features](#features)
- [Technologies](#technologies)
- [Setup & testing](#setup)  

  
<a name="general-info"></a>
# General info

I created this project for educational purposes to get familiar with some of the frontend technologies and to practice establishing the connection between the backend and the frontend. 
The time tracker app is one of my favorite productivity boosters, so I decided to design one by myself. In programming, dealing with time and date might become pretty tricky, so it was a really valuable exercise for me.


<a name="live-demo"></a>
# Live demo: [Trackerrr app.](https://determined-benz-4c7ce5.netlify.app/) 

### A sample account with some projects and time entries created:

### username: testuser
### password: test4321 


 
Because the project is deployed to the Heroku free service, the initial request may take up to 30 seconds.


<a name="screenshots"></a>
# Screenshots:
![Time tracker screenshot](https://res.cloudinary.com/dgmcox/image/upload/v1648665695/timeTrackerSetDate_aipwiq.png)
![Dashboard screenshot](https://res.cloudinary.com/dgmcox/image/upload/v1648665892/dashboard_tylgtl.png)

<a name="features"></a>
# Features:
A few of the things you can do with Trackerrr:

- create an account 
- track your activities using a stopwatch
- keep the counter alive even if the page is closed - thanks to the cookie saved in your browser
- manually add and delete time entries, change hours and date
- add descriptions to time entries
- see recent activities grouped by days
- create a project and assign time entries to it - you can also choose the color in which your project will be displayed
- see the dashboard with charts displaying entries from a given period
- create, update and delete projects, see how much time you spent on each


<a name="technologies"></a>
# Technologies:

The project uses Django with Django Rest Framework and PostgreSQL on the backend, Vue2 and Buefy on the frontend. The authentication is supported by the JWT token. Deployed to Heroku and Netlify. Tests are supported by Cypress on the frontend and unittest on the backend.

Full list of used technologies:
- Python 3.10.3
- Django 4.0.3
- Django Rest Framework 3.13.1
- Django Rest Framework SimpleJWT 4.8.0
- Vue 2.6.11
- Vue Router 3.2.0
- Vuex 3.6.2
- Chart.js 2.9.4
- Axios 0.25
- Buefy 0.9.14
- Bulma 0.9.0
- unittest
- Jest
- Cypress



<a name="setup"></a>
# Setup & testing

## Setup

To run this project locally with the PostgreSQL database:
```bash
$ docker-compose up
```
The app should be accessible at localhost:8080.

## Django tests

Once the project is running inside the docker containers,  you can execute some tests. To do so, open a new terminal and type:
```bash
$ docker exec -it timetracker_backend_1 sh
$ python manage.py test	
```
This will connect to the container which contains django and execute basic tests against the models and API. 

## Cypress e2e tests

You can also run Cypress e2e tests in a docker container:
```bash
$ cd frontend/
$ npm run docker:test:e2e
```
![Cypress tests](https://res.cloudinary.com/dgmcox/image/upload/v1648670851/Screenshot_from_2022-03-30_20-36-11_xpibme.png)

