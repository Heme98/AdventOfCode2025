# AoC 2025 - Heme98

from pathlib import Path

def find_accessible_positions(data: str):
    accessible_count = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            number_of_adjacent_rolls = 0
            if char != "@":
                continue
            # Check left
            if col != 0 and data[row][col - 1] == "@":
                number_of_adjacent_rolls += 1
            # Check right
            if col != len(line) - 1 and data[row][col + 1] == "@":
                number_of_adjacent_rolls += 1
            # Check up
            if row != 0 and data[row - 1][col] == "@":
                number_of_adjacent_rolls += 1
            # Check down
            if row != len(data) - 1 and data[row + 1][col] == "@":
                number_of_adjacent_rolls += 1
            # check diagonals
            # up-left
            if row != 0 and col != 0 and data[row - 1][col - 1] == "@":
                number_of_adjacent_rolls += 1
            # up-right
            if row != 0 and col != len(line) - 1 and data[row - 1][col + 1] == "@":
                number_of_adjacent_rolls += 1
            # down-left
            if row != len(data) - 1 and col != 0 and data[row + 1][col - 1] == "@":
                number_of_adjacent_rolls += 1
            # down-right
            if row != len(data) - 1 and col != len(line) - 1 and data[row + 1][col + 1] == "@":
                number_of_adjacent_rolls += 1
            if number_of_adjacent_rolls < 4:
                accessible_count += 1
    return accessible_count
        
def find_accessible_positions_part2(data: str):
    all_accessible_counts = 0
    while True:
        accessible_count = 0
        indexes_to_modify = []
        for row, line in enumerate(data):
            for col, char in enumerate(line):
                number_of_adjacent_rolls = 0
                if char != "@":
                    continue
                # Check left
                if col != 0 and data[row][col - 1] == "@":
                    number_of_adjacent_rolls += 1
                # Check right
                if col != len(line) - 1 and data[row][col + 1] == "@":
                    number_of_adjacent_rolls += 1
                # Check up
                if row != 0 and data[row - 1][col] == "@":
                    number_of_adjacent_rolls += 1
                # Check down
                if row != len(data) - 1 and data[row + 1][col] == "@":
                    number_of_adjacent_rolls += 1
                # check diagonals
                # up-left
                if row != 0 and col != 0 and data[row - 1][col - 1] == "@":
                    number_of_adjacent_rolls += 1
                # up-right
                if row != 0 and col != len(line) - 1 and data[row - 1][col + 1] == "@":
                    number_of_adjacent_rolls += 1
                # down-left
                if row != len(data) - 1 and col != 0 and data[row + 1][col - 1] == "@":
                    number_of_adjacent_rolls += 1
                # down-right
                if row != len(data) - 1 and col != len(line) - 1 and data[row + 1][col + 1] == "@":
                    number_of_adjacent_rolls += 1
                if number_of_adjacent_rolls < 4:
                    indexes_to_modify.append((row, col))
                    accessible_count += 1
        if accessible_count == 0:
            return all_accessible_counts
        # Modify data in place for next iteration
        for row, col in indexes_to_modify:
            data[row][col] = "."

        all_accessible_counts += accessible_count

def part_one(data: str):
    instructions = data.strip().split('\n')
    return find_accessible_positions(instructions)

def part_two(data: str):
    instructions = data.strip().split('\n')
    matrix = [list(row) for row in instructions]
    return find_accessible_positions_part2(matrix)

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