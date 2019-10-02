# index-map-3d-api

## Quick start

### Docker

This app supports the [common dev-env](https://github.com/LandRegistry/common-dev-env) so adding the following to your dev-env config file is enough:

```YAML
  lender-management-api:
    repo: git@git.dev.ctp.local:digital-street/3d-index-map-api.git
    ref: master
```

The Docker image it creates (and runs) will install all necessary requirements and set all environment variables for you.

## Test Data

This application uses a Postgres database. To populate it, run the following command from the common-dev-env folder:

```shell
bashin index-map-3d-api
make db
```

To view the test data, connect via psql: `psql registerdb`
