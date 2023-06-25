from abstract_validator import validator
from dir_validator import validate_dir


# Hardcoded hash for comparison
HASH = "c1ae8ff2df66f9da7f04a79528bddb4a"


@validator("Data directory unzipped correctly")
def validate():
    return validate_dir("./data", HASH)

if __name__ == "__main__":
    validate()
