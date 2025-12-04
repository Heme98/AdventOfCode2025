# AoC 2025 - Heme98

from pathlib import Path

def get_highest_joltage(banks: str, number_of_batteries: int) -> str:
    highest_joltage = 0
    for bank in banks:
        stack = []
        allowed_skips = len(bank) - number_of_batteries
        for battery_joltage in bank:
            while stack and stack[-1] < battery_joltage and allowed_skips > 0:
                stack.pop()
                allowed_skips -= 1
            stack.append(battery_joltage)
        highest_joltage += (int("".join(stack[:number_of_batteries])))
    return highest_joltage

def part_one(data: str):
    instructions = data.strip().split('\n')
    return get_highest_joltage(instructions, number_of_batteries=2)

def part_two(data: str):
    instructions = data.strip().split('\n')
    return get_highest_joltage(instructions, number_of_batteries=12)

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