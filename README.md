## HeaddressFlyableDeputyBogged

### Techologies: Postgres (Postgis), Python, Node.js, Express, Typescript, Docker

The postgres folder contains a dockerfile that installs postgres with postgis extension, as well as python scripts that import shape files into postgis.
The api folder contains a Dockerized Node.js Express backend that handles requests through API endpoints.


 ``` 
 docker-compose up --build 
 ```

Install pipenv for dependency management in the python script
https://pipenv.pypa.io/en/latest/

 
``` 
cd postgres && pipenv install 
```

Run the first python script to load data into the databse:

``` 
pipenv run python run.py
pipenv run python coverage.py
```


