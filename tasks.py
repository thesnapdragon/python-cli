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


@task
def lint(ctx):
    commands = (
        "flake8 &&"
        "pylint -r n lib &&"
        "pylint -r n misc"
        )
    ctx.run(commands)
