# URL shortener application
# Author: Bálint Maróti

# Requirements

pip install flask flask_sqlalchemy flask-swagger-ui

# Suggested for database visualization:

pip install sqlitebrowser

# Run
python app.py

# Description

This is a simple URL shortener application. It uses a SQLite database to store the original URLs and shorcodes. The application is built with Flask and uses the Flask-SQLAlchemy extension to interact with the database. The application also has a Swagger UI to document the API endpoints.


# API Documentation
The documentation can be found http://127.0.0.1:8000/api/docs/#/ after running the application.

# References
- https://www.youtube.com/watch?v=iZ2Tah3IxQc SBDCODE - Add Swagger UI to Python Flask API
- https://realpython.com/tutorials/flask/ Real Python - Flask Tutorials
- Github Copilot, - Copilot was prompted to use the @workspace and first generate the structure of the swagger.json file, then the specifics were completed manually by the author.
