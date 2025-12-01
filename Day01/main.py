# AoC 2025 - Heme98
from pathlib import Path
from enum import Enum

class Protocol(Enum):
    OLD = False
    NEW = True

def unlock_secret_entrance(instructions: list[str], protocol: Protocol) -> int:
    zero_interactions = 0
    dial_pos = 50
    
    for instruction in instructions:
        direction, rot = instruction[0], int(instruction[1:])
        
        # Old protocol, only count when dial reaches exactly zero
        if protocol == Protocol.OLD and dial_pos == 0:
            zero_interactions += 1
        
        # New protocol, count all zero interactions
        if protocol == Protocol.NEW:
            if direction == "L":
                new_pos = dial_pos - rot
                if dial_pos == 0:
                    zero_interactions += (rot // 100)
                elif (new_pos % 100) == 0:
                    zero_interactions += 1 + (rot // 100)
                elif new_pos < 0:
                    zero_interactions += abs(new_pos // 100)
            elif direction == "R":
                zero_interactions += (dial_pos + rot) // 100
                            
        # Update dial position
        dial_pos = (dial_pos + (rot if direction == "R" else -rot)) % 100
                
    return zero_interactions

def part_one(data: str):
    instructions = data.strip().split('\n')
    return unlock_secret_entrance(instructions, protocol=Protocol.OLD)

def part_two(data: str):
    instructions = data.strip().split('\n')
    return unlock_secret_entrance(instructions, protocol=Protocol.NEW)

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