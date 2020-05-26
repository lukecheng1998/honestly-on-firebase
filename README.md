# honestly-on-firebase
Welcome to Honestly on Firebase where we will be moving the famously honestly project from mongodb to google's firebase!
In addition I will be using 
# Folders and Files
In the Functions Folder 
    In the handlers Folder:
        This contains our search.js file which will read/write database and then call the .py file and store the data result to the database as well
    In the Util Folder:
        This contains our admin and config.js that help us connect to google's firebase
    Index.js the main js file that calls the various functions
    search.py the main python file that will search the internet based on the data filled in the textfield then it will scrape the data and filter words related