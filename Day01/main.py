import Utils.utils

def apply_rotation(rotation: list[str], new_protocol: bool) -> int:
    exactly_zero = 0
    zero_interaction = 0
    start_value = 50
    
    for r in rotation:
        direction, amount = r[0], int(r[1:])
        
        # Old protocol, only count when reaching exactly zero
        if not new_protocol and start_value == 0:
            exactly_zero += 1
        
        # New protocol, count all zero interactions
        if new_protocol:
            if direction == "L":
                zero_interaction = zero_interaction + (abs((start_value - amount) // 100))
                    
            elif direction == "R":
                zero_interaction = zero_interaction + ((start_value + amount) // 100)
        
        # Update starting positions
        if direction == "L":
            start_value = (start_value - amount) % 100
            
        elif direction == "R":
            start_value = (start_value + amount) % 100
                
    if new_protocol:
        return zero_interaction
    
    return exactly_zero


def part_one(data: str):
    ln = Utils.utils.lines(data)
    value = apply_rotation(ln, new_protocol=False)
    return value

def part_two(data: str):
    ln = Utils.utils.lines(data)
    value = apply_rotation(ln, new_protocol=True)
    return value

def main():
    # data = Utils.utils.read_input("Day01/test_input.txt")
    data = Utils.utils.read_input("Day01/real_input.txt")
    print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))

if __name__ == "__main__":
    main()
