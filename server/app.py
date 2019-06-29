"""
Main file to be split into smaller components once proof of concept proves the concept
"""
import importlib
import math
from random import Random
from typing import List

from flask import Flask, jsonify, request
from flask_cors import CORS

import problem_manager
from problem import Problem
from widget import Widget

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


@app.route("/generate/<problem_type>")
def hello(problem_type):
    args = request.args.to_dict()
    args_formatted = {}
    for arg_key in args:
        arg_formatted = format_arg_key(arg_key)
        arg_value_formatted = format_arg(args[arg_key])
        args_formatted[arg_formatted] = arg_value_formatted

    response = problem_manager.registered_problem_types[problem_type].fun(
        **args_formatted
    )
    response_serialized = response.serialize()

    return jsonify(response_serialized)


def main():
    problem_manager.load_problems()
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
