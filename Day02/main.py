# AoC 2025 - Heme98

from pathlib import Path
from enum import Enum

class SubstringsRepeat(Enum):
    ONLY_TWICE = "only_twice"
    TWICE_OR_MORE = "twice_or_more"

def find_new_invalid_ids(id_ranges: str, repeat_frequency: SubstringsRepeat):
    invalid_ids = 0
    for id_range in id_ranges:
        low_bound, high_bound = id_range.strip().split('-')
        for current_value in range(int(low_bound), int(high_bound) + 1):
            value = str(current_value)
            value_length = len(value)
            mid_point = value_length // 2
            
            if repeat_frequency == SubstringsRepeat.ONLY_TWICE:
                if value[:mid_point] == value[mid_point:]:
                    invalid_ids += current_value
                    continue

            elif repeat_frequency == SubstringsRepeat.TWICE_OR_MORE:
                for seq_size in range(1, mid_point + 1):
                    if value_length % seq_size == 0:
                        sequence = value[:seq_size]
                        if sequence * (value_length // seq_size) == value:
                            invalid_ids += current_value
                            break                    
    return invalid_ids
            
def part_one(data: str):
    instructions = data.strip().split(',')
    return find_new_invalid_ids(instructions, repeat_frequency=SubstringsRepeat.ONLY_TWICE)

def part_two(data: str):
    instructions = data.strip().split(',')
    return find_new_invalid_ids(instructions, repeat_frequency=SubstringsRepeat.TWICE_OR_MORE)

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