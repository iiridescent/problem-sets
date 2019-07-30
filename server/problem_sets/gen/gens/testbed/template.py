#  Copyright (c) 2019 Thomas Howe

#%%

# Import all of this

#%load_ext autoreload

from problem_sets import (
    create_full_text_problem,
    debug,
    gen_def,
    Environment,
)


#%%
# %autoreload 2


@debug
# Problem type decorator (don't uncomment this until it's ready to be tested on the server, because the server will import it):
@gen_def(
    description="Example problem type",
    source="Example source",
    target_env=Environment.debug,
)
def example_testbed_problem_type():
    problem_instruction = "Example problem instruction:"

    problem_text = "Example problem content."
    solution_text = "Example problem solution."

    debug_info = [{"example debug info": None}]

    return create_full_text_problem(
        [problem_instruction, problem_text], [solution_text], debug_info
    )
