# How To Handle Frames In Playwright Python

This repository contains code to demo handling of frames in Playwright Python 🎭

The entire testing was performed on local gird as well as [LambdaTest Cloud Grid](http://www.lambdatest.com?fp_ref=jaydeep88)
## Version Check

The code has been fully tested on the below versions

🐋 PyTest 7.3.1

🐍 Python 3.10.1

🎭 Playrwright 1.33

## Env File
The ``secrets.env`` file needs to be amended to run the test on cloud grid by providing the username and access key. 

The varriable ``RUN_ON`` can either have value local or cloud and based on that the tests will be run locally or on cloud grid

The variables ``BROWSER`` and ``PLATFORM`` can be used to set the operating system and browser when running tests on cloud grid

## Running the tests locally 
Set the variable ``RUN_ON=local`` in ``secrets.env`` and run the command

``pytest -v``

## Running the tests on cloud grid
Set the variable ``RUN_ON=cloud`` in ``secrets.env`` and run the command

``pytest -v``
