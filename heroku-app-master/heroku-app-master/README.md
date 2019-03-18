# Heroku App

A basic Django app which has an embedded Vue.js app that can easily be deployed to Heroku.

The best place to start is with the Python documentation for [Getting Started with Python](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true).

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org).
To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli),
as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup) and [Node.js](https://nodejs.org/en/download/).

## Setup

Install the [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) if you don't already have it. Then clone this GitHub repository.
```bash
git clone https://github.com/johnkntran/heroku-app.git
cd heroku-app
```

Create a *virtualenv* for an isolated Python environment.
```bash
python -m venv .venv
source ./venv/Scripts/activate
pip install -r requirements.txt
```

Also, install all JavaScript dependencies.
```bash
npm install
```

Login to Heroku. Then create a heroku app of your own.
```bash
heroku login --interactive
heroku create
```

Run the Django database migrations to create a new sqlite file.
```bash
python manage.py migrate
```

Create a file called .env to store local environment variables, such as `DATABASE_URL` and `NODE_ENV`. The Production version for these values can be found on the [Heroku Dashboard](https://dashboard.heroku.com).
```bash
touch .env
# Edit the .env file to add local variables
# such as DATABASE_URL and NODE_ENV
```

Finally, launch the app using `npm start`. The **Django** portion should be running on [localhost:5000](http://localhost:5000/). The **Vue.js** portion should be running on [localhost:5000/vue/](http://localhost:5000/vue/).

## Deploying to Heroku

To deploy your changes to Heroku and see the live site, follow these steps.

```bash
git push heroku master
heroku open
```

## Loading NPM for Vue Build

To build and deploy the Vue.js application within Django on the Heroku server, both the Node.js and the Python buildpacks must be loaded. Run these commands:

```sh
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 heroku/nodejs
```

For Node.js applications, the `build` script will run automatically. For more information, see these article.

- [Using Multiple Buildpacks](https://devcenter.heroku.com/articles/using-multiple-buildpacks-for-an-app)
- [Node.js deploys will run "build" script automatically beginning March 11](https://help.heroku.com/P5IMU3MP/heroku-node-js-build-script-change-faq)

## Useful Commands

```bash
heroku login --interactive           # Login to Heroku
heroku create <name>                 # Create a new Heroku app
git push heroku master               # Push changes to Heroku cloud
heroku logs --tail                   # View logs
heroku ps:scale web=1                # Scale app to one web instance
heroku ps                            # Check dynos
heroku run python manage.py shell    # Start remote Python shell
heroku run bash                      # Start remote Bash shell (in one-off dyno)
heroku config                        # View production configs
heroku pg                            # Inspect database provision
heroku pg:psql                       # Run a psql shell
heroku open                          # Open production instance (incurs usage)
heroku local web -f Procfile.windows # Run app locally
```

Here is a [list of all commands](https://devcenter.heroku.com/articles/heroku-cli-commands)
