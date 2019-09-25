# Problem Sets API server and static server

## Running in production

To run the Vue client in `client`:

- Install all dependencies with `npm install`
- Build client with `npm run build`
- Install `serve` with `npm install -g serve`
- Run `client.bat`/`client` from the root directory

To run the Python server in `server`:

- Create a virtual environment with virtualenv---the folder should be `venv`
- Run `activate.bat`/`activate` from the root directory to enter the virtual environment
- Install dependencies with `pip install -r requirement.txt`
- Run `server.bat`/`server` from the root directory

(on Linux) to run both in a vertically split `tmux` session, just run `run.sh`.

## Threading issues

For now, run the Flask server with `--without-threads`. I'm looking into ways to allow threaded Flask requests without SQLAlchemy locking the SQLite database. I don't want to use Flask-SQLAlchemy because it requires the server API logic to manage the SQLAlchemy session---this prevents me from building my Flask API on top of an abstract library model.
