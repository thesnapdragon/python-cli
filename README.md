# Python CLI scaffold

## Setup

1. Create `.env` file and set the following environment variables:

    ```
    MYSQL_ROOT_PASSWORD=root
    MYSQL_DATABASE=clidb
    MYSQL_USER=cli
    MYSQL_PASSWORD=password
    MYSQL_HOST_ADDRESS=127.0.0.1
    MYSQL_PORT=3306
    ```
2. Install local Python version with *pyenv*:

    ```
    $ pyenv install 3.5.0
    ```
3. Create *virtualenv*:

    ```
    $ pyenv virtualenv 3.5.0 python-cli
    $ echo python-cli > .python-version
    ```
4. Install *invoke* job runner:

    ```
    $ pip install invoke
    ```

### Production

Install the app:

    ```
    $ inv install
    ```

### Development

1. Install requirements:

    ```
    $ inv init --development
    ```
2. Start MySQL in a Docker container:

    ```
    $ docker-compose create
    $ docker-compose start
    ```
3. Run the *alembic* migrations:

    ```
    $ inv migrate
    ```
