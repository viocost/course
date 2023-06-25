import os
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def md5_dir(path):
    hashes = []
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = md5(file_path)
            hashes.append(file_hash)
    return hashlib.md5("".join(hashes).encode()).hexdigest()


def validate_dir(dir_path, expected_hash):
    computed_hash = md5_dir(dir_path)
    res = computed_hash == expected_hash
    if not res:
        print(f"Computed hash: {computed_hash}\nExpected hash: {expected_hash}")
    return res
