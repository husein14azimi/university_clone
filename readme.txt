this repository is because the previous one got a little bit messed up.


welcome to my first postgre django project!

this project is a simple api. the project includes two main web applications: core and course. the authentication flow is modified by extending the default django abstract user in the 'core.models'. this way, the email field is unique and therefore required for each user (phone number is not implemented yet; maybe i implement it using regex in charfield). the famous technologies you will be seeing in this project are:
    postgreSQL
    independent web apps
    api
    swagger
    postman

using swagger, we will have a full list of allowed requests on each endpoint. using postman, we will see the result of each url.


postgre cli command for creating a new database:

sudo -u postgres psql
CREATE DATABASE your_database_name;
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;
\q




the tokens for a test user:
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMDkyNjYyOCwiaWF0IjoxNzMwODQwMjI4LCJqdGkiOiIwMzI5NzlhYjRkY2M0ZmE3YjZkOWEwMzk1NGI1ZjJjOSIsInVzZXJfaWQiOjJ9.RCzCVBBkRxTmuqf8QbZ-LUTElivjJIZbLmKPDCsUyuo",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwODQwNTI4LCJpYXQiOjE3MzA4NDAyMjgsImp0aSI6IjMwZmQyZTkzYTMwODQ0ZmZiYTI1Mjg5MGM5NDhkZjUxIiwidXNlcl9pZCI6Mn0.7dYmF9GU762Azs-OdxjUX071PDM5eNSNDtEru2z0ymQ"
}