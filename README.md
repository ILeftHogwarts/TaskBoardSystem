TaskBoardSystem
===============
Simple app for task tracking


To run application
Set up environment variables

Windows
set FLASK_APP=main
set FLASK_ENV=development

Linux/MacOS
export FLASK_APP=main
export FLASK_ENV=development


flask run


TODO
=====

+ On shutdown event and close db connection
Tests with mocked data (in memory database and clear data)
Config files and environment variables structure and move credentials to env variables
Serializer mixin
Validation mixin
Check flake8
Check if there is another way to set up db layer(kinda weird to hold db_session in open scope)
Swagger


