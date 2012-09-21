gae-boilterplate
================

Project skeleton for a python based Google App Engine project

Lets break it up and have a look at what a typical web application project requires:

- Configuration storage which can be accessed very easily in the app 
- URL to Request Handler mapping also known as URL routing in some other frameworks.
- Request Handlers: In some framework, they are known as views or controllers/method. Basically a way to define request handling. This is all what a web application does. This is the part in web app which keeps on growing as your app scales.
- Templating Engine:
- Background tasks: which are nothing but a special form of request handlers in case GAE. 
- Static Content: an app serves static component like images, css files and javascript files as well.


Quick description of the project structure (what lies where ?)

- app.yaml - App Engine configuration file
- config.py - This is where app configuration goes. Things like API secrets etc.
- routes.py - Here goes URL mapping. It contains nothing but a list of URL pattern and corresponding request handler class.
- main.py - It binds all of them together. You will not have to change much in this file.
- handlers - Top level directory which contains all of our request handler. We can have sub directories to organize the handlers. You can start with files first and then create folders as your app scales up.
    -- base.py - This implements BaseHandler class which implements some of the most common functionality required by all the other handlers
    -- *.py
- models - Top level directory which contains all of your data store models.
- static - Top level directory to organize static content
    -- libs 
	-- bootstrap
	-- jquery
	-- backbone
	-- jqueryui
    -- app
	-- css
	-- js
	-- images	
- templates - Top level directory containing all of your HTML templates. This project uses Mako templating framework.
    -- base.html an HTML file which defines the HTML skeleton which needs to be inherited by all other HTML files
    -- *.html
- tools - This directory should be used to store all of your scripts related to the project. A few examples
	-- scripts to download/upload application data from production
	-- etc.
- libs - This directory should contain all the external python packages you want to bundle in your app. For ex. in this sample, I have bundled mako templating framework