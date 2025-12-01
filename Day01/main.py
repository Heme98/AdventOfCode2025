# AoC 2025 - Heme98
from pathlib import Path

def count_zero_interactions(instructions: list[str], count_all_interactions: bool) -> int:
    zero_interactions = 0
    dial_pos = 50
    
    for instruction in instructions:
        direction, rot = instruction[0], int(instruction[1:])
        
        # Old protocol, only count when reaching exactly zero
        if not count_all_interactions and dial_pos == 0:
            zero_interactions += 1
        
        # New protocol, count all zero interactions
        if count_all_interactions:
            if direction == "L":
                # If at zero, count how many times we pass zero again
                if dial_pos == 0:
                    zero_interactions += (rot // 100)
                # If we land exactly on zero, count that plus how many times we passed zero
                elif ((dial_pos - rot) % 100) == 0:
                    zero_interactions += 1 + (rot // 100)
                # If we pass zero but don't land on it only count the passes
                elif dial_pos > 0:
                    zero_interactions += abs((dial_pos - rot) // 100)
                    
            elif direction == "R":
                zero_interactions += (dial_pos + rot) // 100
                            
        # Update starting positions
        if direction == "L":
            dial_pos = (dial_pos - rot) % 100
            
        elif direction == "R":
            dial_pos = (dial_pos + rot) % 100
                
    return zero_interactions

def part_one(data: str):
    instructions = data.strip().split('\n')
    return count_zero_interactions(instructions, count_all_interactions=False)

def part_two(data: str):
    instructions = data.strip().split('\n')
    return count_zero_interactions(instructions, count_all_interactions=True)

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