from abstract_validator import validator
from dir_validator import validate_dir

@validator("Used wildcard to copy files with similar prefix")
def validate():
    return validate_dir("submission/bravo", "fb2194bd44320a3bf579061da492c7e8")



if __name__ == "__main__":
    validate()
