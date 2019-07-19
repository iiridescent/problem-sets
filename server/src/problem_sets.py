import problem_generator_manager

def problem(type_ref: str):
    return problem_generator_manager.registered_problem_types[type_ref].fun()

def initialize():
    problem_generator_manager.load_generators()
