# Base the image on the built-in Azure Functions Python image
FROM mcr.microsoft.com/azure-functions/python:latest

# See the logs when the Function Host is running
ENV AzureFunctionsJobHost__Logging__Console__IsEnabled=true

# Add files from this repo to the root site folder.
COPY . /home/site/wwwroot

# Install requirements
RUN cd /home/site/wwwroot && pip install -r requirements.txt