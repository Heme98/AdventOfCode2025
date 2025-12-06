# AoC 2025 - Heme98

from pathlib import Path

def find_fresh_iems(data: str):
    fresh_ingredient_ids = []
    fresh_items = 0
    for item in data:
        if item == "":
            continue
        
        if "-" in item:
            start, end = map(int, item.split("-"))
            fresh_ingredient_ids.append([start, end])
            continue
        
        for start, end in fresh_ingredient_ids:
            if start <= int(item) <= end:
                fresh_items += 1  
                break  
    return fresh_items

def find_all_fresh_ids(data: str):
    fresh_ingredient_ids = []
    for item in data:
        # early exit on empty line
        if item == "":
            break
        
        if "-" in item:
            start, end = map(int, item.split("-"))
            fresh_ingredient_ids.append((start, end))
            
    # Check overlapping ranges and merge them
    merged_ranges = []
    for start, end in sorted(fresh_ingredient_ids):
        if not merged_ranges or merged_ranges[-1][1] < start - 1:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

    return  sum(end - start + 1 for start, end in merged_ranges)


def part_one(data: str):
    instructions = data.strip().split('\n')
    return find_fresh_iems(instructions)

def part_two(data: str):
    instructions = data.strip().split('\n')
    return find_all_fresh_ids(instructions)

def main():
    """Run solutions on test and real inputs."""
    base_path = Path(__file__).parent
    
    # Test input
    test_data = (base_path / "test_input.txt").read_text()
    print("\n=== Test Results ===")
    print(f"Part 1: {part_one(test_data)}")
    print(f"Part 2: {part_two(test_data)}")
    
    # Real input
    real_data = (base_path / "real_input.txt").read_text()
    print("\n=== Real Results ===")
    print(f"Part 1: {part_one(real_data)}")
    print(f"Part 2: {part_two(real_data)}")

if __name__ == '__main__':
    main()