# Running Server
For running application there are 2 option:
1. for running server locally, just run ```python3 wsgi.py```
2.  for running server by anywhere ip just run
        ```./start_gunicorn.sh```, you could adjust the worker that should be used by change ```-w worker_number```
        where worker_number is number of worker

# Generate Database 
if you want to generate database and all the tables just execute 
```make migration_db```, currently the applications use local database

# Collection Postman
all collection postman save in folder collections