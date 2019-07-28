"""
Main file to be split into smaller components once proof of concept proves the concept
"""
import importlib
import math
from random import Random
from typing import List

from flask import Flask, jsonify, request
from flask_cors import CORS

import problem_sets as sets
from problem_sets import Environment, problem
from json import dumps


app = Flask(__name__)
CORS(app)


# We need to have the option to ask multiple questions about one piece of information
# So we could have a function that asks different things about functions
# a) what is the absolute minimum?
# b) what are the x-intercepts, if any?
# c) what is the domain of this function?
# Et cetera...

# Additionally, we need to define a format that uses JSON nodes, so we can display elements like graphs
# Any widgets we define will need to have handlers on the client side.


def format_arg_key(arg):
    return arg.replace("<br>", "").replace("-", "_")


def format_arg(arg):
    return arg.replace("<br>", "")


@app.route("/api/problem/<set_id>")
def hello(set_id):
    # args = request.args.to_dict()
    # args_formatted = {}
    # for arg_key in args:
    #     arg_formatted = format_arg_key(arg_key)
    #     arg_value_formatted = format_arg(args[arg_key])
    #     args_formatted[arg_formatted] = arg_value_formatted

    response = sets.problem(set_id)
    response_serialized = response.serialize()

    print(dumps(response.debug_info, indent=4, separators=(",", ": ")))

    print(response_serialized)

    return jsonify(response_serialized)


def main():
    sets.initialize(Environment.debug)
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()