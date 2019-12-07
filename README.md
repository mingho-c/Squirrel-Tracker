![](https://media.npr.org/assets/img/2017/04/25/istock-115796521-fcf434f36d3d0865301cdcb9c996cfd80578ca99-s800-c85.jpg)
# Squirrel-Tracker Web Application

## General Description
The Squirrel-Tracker project is to design a web application with multiple features using the django framework. The main purpose is to keep track of all the known squirrels at the Central Park in a flexible and comprehensive way. 
It allows users to import the [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) data and to view, add and update squirrel data.
It can also display the location of the squirrel sightings on an [OpenStreets map](https://www.openstreetmap.org/about/).


## App Features
### Management Commands
* Import Command
  + Description: A command that can be used to import the data from the 2018 Central Park Squirrel Census.
  + Location: *management/commands/*
  + Usage: The file path should be specified at the command line after the name of the management command. 
    + i.e. *$ python manage.py import_squirrel_data /path/to/file.csv*

* Export Command
  + Description: A command that can be used to export the data in CSV format. 
  + Location: *management/commands/*
  + Usage: The file path should be specified at the command line after the name of the management command. 
    + i.e. *$ python manage.py export_squirrel_data /path/to/file.csv*


### Views
* Map
  + Description: A view that shows a map that displays the location of the squirrel sightings. 
  + Location: */map*
  + Usage: It uses the [leaflet library](https://leafletjs.com/) for plotting. 
  + Note: The browser will start to freeze if plotting more than 100 points at once.
  
* All
  + Description: A view that lists all squirrel sightings with links to edit each. It also has a single link to the "add" sighting view.
  + Location: */sightings*
  + Usage: Other than the links to edit each squirrel sightings on the page, users can also click on the "Create a New Sighting" link to add a new squirrel sighting.
  
* Update
  + Description: A view to update a particular sighting. 
  + Location: */sightings/unique-squirrel-id*
  + Usage: Users can click on the 'edit' button to update a squirrel sighting on the page.
  
* Add
  + Description:  A view to create a new sighting. 
  + Location: */sightings/add*
  + Usage: Users can click on the 'edit' button to create a new squirrel sighting on the page.
  
* Stats
  + Description: A view with general stats about the sightings. It displays five of the attributes listed in the initial CSV download.
  + Location: */sightings/stats*
  + Usage: Users can quickily learn about the general information of the squirrel data.


## Project Group and UNIs
* Project Group 24, Section 1

* UNIs: [kl3174, mc4793]


## Server Link
!!needs to be inserted!!

[](https://<your project id>.appspot.com/)

