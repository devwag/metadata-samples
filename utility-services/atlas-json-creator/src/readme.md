# Build the docker image with the application code embedded
```
docker build -f <project root>/docker/Dockerfile . -t atlas-json-creator
```

# Run docker image
```
docker run -it -p 7171:80 atlas-json-creator
```

# Test HttpTrigger
```
$> curl http://localhost:7171/api/HttpTrigger
Atlas Json Creator function is up and running.%
```