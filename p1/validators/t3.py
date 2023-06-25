from abstract_validator import validator
from dir_validator import validate_dir

@validator("directory juliet-444/tango-909 copied to submission/alpha recursively")
def validate():
    return validate_dir("submission/alpha/tango-909", "af525fdecccc6576fcf478432fc72c8d")



if __name__ == "__main__":
    validate()
