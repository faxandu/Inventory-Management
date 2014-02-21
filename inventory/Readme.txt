greetings future tech! this readme is here to try and give you some idea of the framework we 
used in the creation of parts of the site. few things to get out of the way:

this is django version 1.5.1

when doing an yum/apt-get install, the package is "django==1.5.1"

I am also assuming you know enough linix to use it by the command line.

if you just pulled this code from git, and want to launch a local test server for ease
of changing the code, follow these steps:

cd to where ever you pulled the project folder, but don't go into it

virtualenv Inventory_Management

wait for it to finish

cd Inventory_Management

source bin/activate

pip install django==1.5.1

once again wait for it to finish

cd inventory

python manage.py runserver

that will get you a test server set up locally, just open a brower and go to the URL that is in the 
command window (you can ctrl+click it as well)

the following is a list of relevent files that should be the ones you look at when you want to
modify the code. ill try to be breif but detailed

-----in the folder "inventory"
this holds the files that modify a site as a whole, as djano apps are seperate in there 
functionality we don't "need" to touch anything here, as this is just one app on the side. but
ill outline the two relevent files here

---settings.py
this file holds the settings for a site, such as where files are stored when uploaded, which
database to use, and which apps are installed(the variable is called INSTALLED_APPS). if you are
just playing with the inventory system, don't mess with anything here.

---urls.py
specifies which URL's when entered in a browser provide hits to a site. these use 
regular expressions, we use simple ones so it shouldent be that bad to look at. when a url
matches one of the expressions, it "chop" the part that matches and passes it to the OTHER
url file (which is in the other directory, linked in this file)

-----in the folder "Inventory_Management"
this folder is the "app" part of the site that holds all the information about the inventory
session. the chain of files are: urls.py -> views.py -> models.py

---urls.py
this is the same as the one from the other directory, it takes that part that wasen't chopped off
and it is passed into this file, where the process is repeated, it finds a match on a regular
expression and calls the FUNCTION out of the VIEWS file as specified.

---views.py
these holds functions that do the work. they modify the database, perform querys, and retuen
relevent information. the (request) you see in all of the functions here are what is passed
in from a front end. if you know much about webcodeing, this variable brings in a POST request
set of data, accessed via request.POST['fieldinpost']. more details in the file

---models.py
here is where the database tables are actualy defined. its a relational database, details on that
in the file.
