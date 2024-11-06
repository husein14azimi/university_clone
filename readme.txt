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



urls for authentication and profile:
    register:
    /auth/users/

    login:
    /auth/jwt/create/

    profile:
    /account/persons/


the tokens for a test user:

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMDk2NTY1NCwiaWF0IjoxNzMwODc5MjU0LCJqdGkiOiI3NmVkNGZjZTM1YmU0ZDcyODRkZDZjZDAzMjQ1OWFkMSIsInVzZXJfaWQiOjJ9.ng-Hv3dFpTPsz2t83TOWQedXA_G6bFTF-jvadi0-I9w",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwODgyOTI0LCJpYXQiOjE3MzA4NzkyNTQsImp0aSI6ImQ0ZGQ4MDg1NDIzOTQwODA4NzczYjcwNTg2NTdiN2RiIiwidXNlcl9pZCI6Mn0.ytccJD8D-tOZHdzayynGyXLqyKELOdyTAIi122uyN9o"
}