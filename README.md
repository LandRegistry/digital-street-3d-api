# digital-street-3d-api

## Quick start

### Docker

This app supports the [common dev-env](https://github.com/LandRegistry/common-dev-env) so adding the following to your dev-env config file is enough:

```YAML
  digital-street-3d-api:
    repo: git@github.com:LandRegistry/digital-street-3d-api.git
    ref: master
```

The Docker image it creates (and runs) will install all necessary requirements and set all environment variables for you.

## Test Data

This application uses a Postgres database. To populate it, run the following command from the common-dev-env folder:

```shell
bashin digital-street-3d-api
make db
```

To view the test data, connect via psql: `psql registerdb`

## Updating Postgres on Heroku

First, reset the database using Heroku's Postgres plug-in, then enter the following commands into the Heroku app's bash console:

```shell
export SQL_USE_ALEMBIC_USER=yes && export SQL_PASSWORD={PG_PASSWORD} && python3 manage.py db upgrade
PGPASSWORD={PG_PASSWORD} psql -h {PG_HOSTNAME} -U {PG_USERNAME} -d {PG_DATABASE_NAME} -f setup_db.sql;
```