# Comments API

This project is intended to be a simple comments microservice deployed ready
to be deployed in AWS using the [serverless framework](https://www.serverless.com/).

This will probably be an overcomplicated version of the api cause I want to
do some experiments to understand how to work with serverless and will probably
add layers of database and authentication.

It will start simple and start building from there. The following section will
contain a description of how is the api working at the moment.

## The API

At the moment this api has 2 functions contained in the file `handler.py` one function
handles the GET request and returns all comments stored for the required key while
the second handles the post request and saves a comment to a given key.

At the moment, they'll handle dummy responses with no persistance. Then a database
layer will be created.
