#!/bin/env python
import os
import sys
import subprocess
import argparse
from termcolor import colored

def run_validators():
    validators_dir = "./validators"
    passed = 0
    failed = 0

    validator_names = sorted([os.path.splitext(filename)[0] for filename in os.listdir(validators_dir) if filename.endswith(".py")])

    for validator_name in validator_names:
        if validator_name in ["abstract_validator", "dir_validator"]: continue
        validator_path = os.path.join(validators_dir, f"{validator_name}.py")

        if not os.path.exists(validator_path):
            print(colored(f"Error: Validator {validator_name} not found", "red"))
            continue

        result = subprocess.run(["python", validator_path], capture_output=True, text=True)
        output = result.stdout.strip().split(",")
        err = result.stderr.strip()

        if len(output) != 2:
            print(colored(f"Error in validator {validator_name}: invalid output", "yellow"))
            print(err)
            continue

        result, description = output
        if result == "pass":
            print(f"  {validator_name} - {description}: ", colored("pass", "green"))
            passed += 1
        elif result == "fail":
            print(f"  {validator_name} -  {description}: ", colored("fail", "red"))
            failed += 1
        else:
            print(colored(f"Error in validator {validator_name}: invalid result", "yellow"))
            failed += 1

    print(f"\n=======================\n  Passed: {passed} ||  Failed: {failed} \n", end=" ")

    if passed > 0 and failed == 0:
        print(colored(" You successfully completed this project!\n", "green"))
    else:
        print(colored("Some of the tests are not passing...  Keep on working! \n", "red"))

if __name__ == "__main__":

    print("\nValidating your work:")
    run_validators()
