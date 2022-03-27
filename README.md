
# Trackerrr - simple, but fully functional time tracker app

## Table of contents

- [General info](#general-info)  
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)  

  
<a name="general-info"/></a>
# General info

I created this project for educational purposes, to get familiar with some of the front-end technologies and practice establishing connection between backend and frontend. 
The time tracker app is one of my favorite productivity booster, so I decided to design one by myself. Dealing with time and date can become pretty tricky, so it was a really good programming exercise for me.


<a name="features"></a>
# Features:
A few of the things you can do with Trackerrr:

- create account 
- track your activities using stopwatch
- keep the counter alive even if the page is closed - thanks to cookie saved in your browser
- manually add and delete time entries, change hours and date
- add descriptions to time entries
- see recent activities groupped by days
- create project and assign time entries to it, you can also choose the color in which your project will be displayed
- see dashboard with charts displaying entries from a given period
- create, update and delete projects, see how much time you spent on each


<a name="technologies"></a>
# Technologies:

The project uses Django with Django Rest Framework and PostgreSQL on the backend, Vue2 and Buefy on the frontend. Authetication is handled by JWT token. Deployed to Heroku and Netlify.

List of used technologies:
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
# Setup:

To run this project locally