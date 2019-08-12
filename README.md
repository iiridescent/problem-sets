# README

## Running in production

To run the Vue client:

- Install `serve` with `npm install -g serve`
- Run `client.bat`/`client`

To run the Python server:

- Run `activate.bat`/`activate` to enter the virtual environment
- Run `server.bat`/`server`

## Threading issues

For now, run the Flask server with `--without-threads`. I'm looking into ways to allow threaded Flask requests without SQLAlchemy locking the SQLite database. I don't want to use Flask-SQLAlchemy because it requires the server API logic to manage the SQLAlchemy session---this prevents me from building my Flask API on top of an abstract library model.
