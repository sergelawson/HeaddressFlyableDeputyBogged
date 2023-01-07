## HeaddressFlyableDeputyBogged

### Techologies: Postgres (Postgis), Python, Node.js, Express, Typescript, Docker

The postgres folder contains a dockerfile that installs postgres with postgis extension, as well as python scripts that import shape files into postgis.
The api folder contains a Dockerized Node.js Express backend that handles requests through API endpoints.


 ``` 
 docker-compose up --build 
 ```
While docker is running open an new tab in your terminal and install pipenv for dependency management in the python script: https://pipenv.pypa.io/en/latest/

 
``` 
cd postgres && pipenv install 
```

Run the first python script to load data into the databse (shapefiles are missing in this repository):

``` 
pipenv run python run.py # import the shape files into the database table fields
pipenv run python coverage.py # create polygon coverage and import into the database table coverage
```


#### Test API Endpoints

- http://localhost:8080/delineated-fields?location=11.190343929175015,60.742178240839934

- http://localhost:8080/delineated-areas
