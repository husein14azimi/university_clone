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
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMDk1NTk4MywiaWF0IjoxNzMwODY5NTgzLCJqdGkiOiIyMmNmOTI2OGQ4ZDM0Yjg3OTNiZjY2NDk2Nzg3YTgyNSIsInVzZXJfaWQiOjJ9.1LPmbtvBUcuoUzSfqPwcpKWsk2qOV4H89c4VZBIzvAQ",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwODY5ODgzLCJpYXQiOjE3MzA4Njk1ODMsImp0aSI6ImI0ODMzYTZhMzJhMTQ4NzI5YmJiZTU3MTYwNzc3ZDE2IiwidXNlcl9pZCI6Mn0.OH9DoZ5lbh3PCVFhlOF5eYyyIVM15aaXhvVFAlZtOz0"
}