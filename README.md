# Python CLI scaffold

## Setup

1. Create `.env` file and set the following environment variables:

~~~ {.bash}
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=clidb
MYSQL_USER=cli
MYSQL_PASSWORD=password
MYSQL_HOST_ADDRESS=127.0.0.1
MYSQL_PORT=3306
~~~

2. Install local Python version with *pyenv*:

~~~ {.bash}
$ pyenv install
~~~

3. Create *virtualenv* and activate the environment:

~~~ {.bash}
$ virtualenv venv
$ source venv/bin/activate
~~~

4. Install *invoke* job runner:

~~~ {.bash}
$ pip install invoke
~~~

### Production

5. Install requirements:

~~~ {.bash}
$ inv init
~~~

6. Run the *alembic* migrations:

~~~ {.bash}
$ inv migrate
~~~

### Development

5. Install requirements:

~~~ {.bash}
$ inv init --development
~~~

6. Start MySQL in a Docker container:

~~~ {.bash}
$ docker-compose create
$ docker-compose start
~~~

7. Run the *alembic* migrations:

~~~ {.bash}
$ inv migrate
~~~
