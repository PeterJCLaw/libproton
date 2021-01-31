from __future__ import print_function

import os
import subprocess

import yaml
import helpers


def get_bacon_scorer():
    my_dir = os.path.dirname(os.path.realpath(__file__))
    bacon_scorer = os.path.join(my_dir, 'data/cli/bacon_scorer.py')
    assert os.path.exists(bacon_scorer), bacon_scorer

    return bacon_scorer


def run(relative_path):
    bacon_scorer = get_bacon_scorer()
    process = subprocess.Popen([bacon_scorer, relative_path],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr


def assert_run(relative_path):
    retcode, stdout, stderr = run(relative_path)
    if retcode != 0:
        print(stderr)

    assert retcode == 0, "Bad return code scoring '{0}'.".format(relative_path)

    result_dict = yaml.load(stdout)
    return result_dict


def check_by_input_file(input_name):
    input_file, expected_output = helpers.get_data('tests/data/cli', input_name)

    output = assert_run(input_file)

    assert output == expected_output, "Incorrect scores for '{0}'.".format(input_name)


def test_input_file():
    inputs = helpers.get_input_files('tests/data/cli')

    for input_name in inputs:
        yield check_by_input_file, input_name


def test_stdin():
    # A proton compliant program MUST consume YAML from stdin
    # if it is not given a filename.

    with open('tests/data/cli/zero.yaml', 'r') as zeros_input:
        with open('tests/data/cli/zero.out.yaml') as f:
            zeros_output = yaml.load(f)

        bacon_scorer = get_bacon_scorer()
        process = subprocess.Popen([bacon_scorer], stdin=zeros_input,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(stderr)

        assert process.returncode == 0, "Bad return code scoring from stdin."

        result_dict = yaml.load(stdout)

        assert result_dict == zeros_output, "Bad output when reading from stdin"


def test_missing_file():
    nope = 'bacon'
    assert not os.path.exists(nope)
    retcode, _, _ = run(nope)
    assert retcode == 1, \
        "Should error when nonexistent input file '{}' is provided.".format(
            nope,
        )
