from invoke import task


@task
def init(ctx, development=False):
    if development:
        ctx.run("pip install -r requirements/development.txt")
    else:
        ctx.run("pip install -r requirements.txt")


@task
def migrate(ctx):
    ctx.run("alembic upgrade head")


@task(post=[init, migrate])
def install(ctx):
    ctx.run("sudo ln -s config/python-cli.conf /etc/init")


@task
def lint(ctx):
    commands = (
        "flake8 &&"
        "pylint -r n db &&"
        "pylint -r n misc &&"
        "pylint -r n tests"
        )
    ctx.run(commands)


@task
def test(ctx):
    ctx.run("nosetests --rednose --force-color")


@task(pre=[lint, test])
def build(ctx):
    pass
