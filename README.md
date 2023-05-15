# Billing System Introduction:

The service is a Billing System using Processor "BlackBox".


## Installation

* Use python 3.8 version. https://www.python.org/downloads/release/python-380/

* Use Docker. https://docs.docker.com/language/python/build-images/


```bash
# Build the Image
docker build -t tasker-fast-api

# Run the Docker
docker run tasker-fast-api
```
* src.apps.Processor.py can be run also using python IDE. (The service)
* src.apps.BillingSystem.py can be run also using python IDE. (The service)


## Fast-API Swagger
To open the Swagger go to  http://127.0.0.1:8000/docs#/

## Notes

* src.lib.exception_handler.Exceptions.py need to be created to give our own Exceptions.
* DB should be completed




