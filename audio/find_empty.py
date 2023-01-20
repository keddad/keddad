from pathlib import Path
import sys
import argparse

from utils import AUDIO_FORMATS

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("path") # Path to musical library

    return parser.parse_args(args)

def check_folder(folder):
    all_files = list(folder.rglob("*"))

    return any(map(lambda x: x.suffix in AUDIO_FORMATS, all_files))

# MusicBrainz is horrible thing that deleted originals of my songs
# So we've got a script to find folders we need to redownload
# Finds folders without any audio files
def main():
    args = parse_args(sys.argv[1:])

    main_folder = Path(args.path)
    folders = list(main_folder.iterdir())
    
    for f in folders:
        if not check_folder(f):
            print(str(f))

if __name__ == "__main__":
    main()