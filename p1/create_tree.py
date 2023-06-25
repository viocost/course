#!/bin/env python
import os
import random
import argparse
from faker import Faker

# NATO phonetic alphabet
NATO_ALPHABET = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", 
                 "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", 
                 "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", 
                 "xray", "yankee", "zulu"]

faker = Faker()

def create_dir_tree(path, depth):
    if depth > 0:
        # Create between 3 and 20 directories
        for _ in range(random.randint(3, 20)):
            # Create directory

            dir_name = f"{random.choice(NATO_ALPHABET)}-{str(random.randint(1, 999)).zfill(3)}"
            dir_path = os.path.join(path, dir_name)

            while os.path.exists(dir_path):
                dir_name = f"{random.choice(NATO_ALPHABET)}-{str(random.randint(1, 999)).zfill(3)}"
                dir_path = os.path.join(path, dir_name)

            os.mkdir(dir_path)

            # Create between 0 and 200 text files in each directory
            file_counts = {word: 0 for word in NATO_ALPHABET}
            for _ in range(random.randint(0, 200)):
                # Create file
                file_word = random.choice(NATO_ALPHABET)
                file_counts[file_word] += 1
                file_name = f"{file_word}-text-{str(file_counts[file_word]).zfill(3)}.txt"
                file_path = os.path.join(dir_path, file_name)
                # Check if file exists, if so, increment the file count and try again
                while os.path.exists(file_path):
                    file_counts[file_word] += 1
                    file_name = f"{file_word}-text-{str(file_counts[file_word]).zfill(3)}.txt"
                    file_path = os.path.join(dir_path, file_name)
                with open(file_path, 'w') as f:
                    # Write random Shakespearian text
                    sentences = faker.sentences(nb=random.randint(4, 12), ext_word_list=None)
                    f.write('\n'.join(sentences))
            # Recurse into subdirectories
            create_dir_tree(dir_path, depth - 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a random directory tree.')
    parser.add_argument('--path', type=str, default='.', help='The root path of the directory tree.')
    parser.add_argument('--depth', type=int, default=5, help='The maximum depth of the directory tree.')
    args = parser.parse_args()

    create_dir_tree(args.path, args.depth)

