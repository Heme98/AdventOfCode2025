#!/usr/bin/env python3
import argparse
import os
import shutil
import sys

def pad(n: int) -> str:
    return f"{n:02d}"

def create_day_folder(n: int):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "template.py")
    
    if not os.path.exists(template_path):
        print("ERROR: template.py not found in script directory.")
        sys.exit(1)

    day_name = f"Day{pad(n)}"
    print(f"Creating {day_name}...")
    os.makedirs(day_name, exist_ok=True)

    # Copy main.py
    dest_main = os.path.join(day_name, "main.py")
    if not os.path.exists(dest_main):
        shutil.copyfile(template_path, dest_main)
        print(f"  Created {dest_main} from template.py")
    else:
        print(f"  {dest_main} already exists, skipping copy.")

    # Create test_input.txt
    test_input_path = os.path.join(day_name, "test_input.txt")
    if not os.path.exists(test_input_path):
        with open(test_input_path, "w") as f:
            f.write("")
        print(f"  Created empty test_input.txt")
    else:
        print(f"  {test_input_path} already exists, skipping.")

    # Create real_input.txt
    real_input_path = os.path.join(day_name, "real_input.txt")
    if not os.path.exists(real_input_path):
        with open(real_input_path, "w") as f:
            f.write("")
        print(f"  Created empty real_input.txt")
    else:
        print(f"  {real_input_path} already exists, skipping.")

    print("Done.\n")

def main():
    parser = argparse.ArgumentParser(
        description="Generate Advent of Code DayXX folder with template and input files"
    )
    parser.add_argument(
        "day",
        type=int,
        help="Day number (e.g., 1 for Day01)"
    )
    args = parser.parse_args()
    create_day_folder(args.day)

if __name__ == "__main__":
    main()
