import os
from abstract_validator import validator

@validator("Submission directory exists")
def validate():
    return os.path.exists('./submission')

if __name__ == "__main__":
    validate()
