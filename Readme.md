### Create a new virtual environment

    virtualen env

### Activate the virtual environment

    source env/bin/activate

### Install modules with

    pip install -r requirements.txt


### Or:

pip freeze | cut -d'=' -f1 > requirements.txt

pip install Flask Flask-PyMongo Flask-JWT-Extended python-dotenv