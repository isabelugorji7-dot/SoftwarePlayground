DJANGO CRASH COURSE 
Resources 
Django documentation
Vs code 

Extensions
prettier code formatter
Auto rename tag

To set up
django-admin 
make migrations 
migrate 
runserver 
start app
start project

KEYS
BIG/MAIN DJANGO FILE - backend
MINI/SMALL DJANGO FOLDER - backend (its the one already inside a backend folder)

1. django-admin startproject project name goes here
2. cd project name - Takes you into the project name
3. python manage.py runserver - Runs the projects server
    ctrl + click on the http://127.0.0.1:8000/ - Takes you into the site
    - You see a rocket and a message saying that the install works
    ctrl + c - Stops the server from running
4. Open a new command prompt and run python manage.py startapp 'insert app name here' - creates a folder for the app name
    - Go to views.py in the second 'folder name here' folder 
5. Go to main project file then settings.py
    - Settings.py in the main folder and tell django about the mini folder inside it
    - In INSTALLED_APPS add the mini folders name like this 'mini folder' 
6. To CREATE/ test out the page [NOT RECOMMENDED I THINK]
    - in the main folders urls.py create a path for the home page.
        - from django.http import HttpResponse
        - You need a function for the home page. 
            - def home(request):
                return HttpResponse('Home page')
        - The function you wrote for the home page will return the request  
        - The urlpatterns for this is 
            path('', home),
            the empty quotation marks is to show django that its a root page the main page it loads up first since its the home page.
- For a different page
    - Create a function sill (eg. room page)
       def room(request):
        return HttpResponse('ROOM') 
    - Create a path for the new page
        path('room/', room)
            - the quotation mark wasn't empty this time it had the specific path i wanted to go to being room/ since its not a root file(home page) it has to be 
                the function name then forward slash
    - this is how it'll look in the http link
    http://127.0.0.1:8000/room/

THIS IS MESSY AND NOT THE BEST FOR BIG PROJECTS.
7. Remove the http response and the functions from the urls.py in the main folder.
8. Go to base folder you made that's the app.
    - Go to views.py
    - Add the functions from before there 
        def home(request):
            return HttpResponse('Home page')

        def room(request):
            return HttpResponse     ('ROOM')
- Go to the base folder and create a urls.py file.
    - This handles all the connections between the base folder app and the url pages

    - Import the django path
        from django.urls import path
        from .import views
    - Create a urlspatterns list 
        urlpatterns = [
            path('', views.home, name="home"),
            path('room/', views.room, name="room"),
        ]
    - In views.py again Import HttpResponse
        from django.http import HttpResponse
    - Configure the pages 
        - In backends urls.py replace from django.urls import pah with from django.urls import path, include the ,include makes it configured also add a path in the urlspatterns to the app your making.
            path('', include('base.urls'))  
9. Templates
    In main project file create a folder called template this is where all the html pages will be stored
        - 




