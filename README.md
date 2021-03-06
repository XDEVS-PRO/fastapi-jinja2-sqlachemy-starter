# fastapi_starter


## Features

* FastAPI
* SQLAlchemy and Alembic
* Pre-commit hooks (black, autoflake, isort, flake8, prettier)
* Github Action
* Dependabot config
* Docker images


## Step 1: Getting started

Start a local development instance with docker-compose

```bash
docker-compose up -d

# Run database migration
docker-compose exec backend alembic upgrade head

# Create database used for testing
docker-compose exec postgres createdb apptest -U postgres
```

Now you can navigate to the following URLs:

- Backend OpenAPI docs: http://localhost:8000/docs/


### Step 2: Setup pre-commit hooks and database

Keep your code clean by using the configured pre-commit hooks. Follow the [instructions here to install pre-commit](https://pre-commit.com/). Once pre-commit is installed, run this command to install the hooks into your git repository:

```bash
pre-commit install
```

### Local development

The backend setup of docker-compose is set to automatically reload the app whenever code is updated.


### Rebuilding containers

If you add a dependency, you'll need to rebuild your containers like this:

```bash
docker-compose up -d --build
```

### Database migrations


These two are the most used commands when working with alembic. For more info, follow through [Alembic's tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html).

```bash
# Auto generate a revision
docker-compose exec backend alembic revision --autogenerate -m 'message'

# Apply latest changes
docker-compose exec backend alembic upgrade head
```

### Backend tests

Backend uses a hardcoded database named apptest, first ensure that it's created

```bash
docker-compose exec postgres createdb apptest -U postgres
```

Then you can run tests with this command:

```bash
docker-compose exec backend pytest
```

## Recipes

#### Build and upload docker images to a repository

Configure the [**build-push-action**](https://github.com/marketplace/actions/build-and-push-docker-images) in `.github/workflows/test.yaml`.


## Credits

Created with [FastAPI Starter](https://github.com/gaganpreet/fastapi-starter)
