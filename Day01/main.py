import Utils.utils

def apply_rotation(rotation: list[str], new_protocol: bool) -> int:
    wrap_arounds = 0
    exactly_zero = 0
    start_value = 50
    
    for r in rotation:
        direction, amount = r[0], int(r[1:])
        
        # Calculate zero crossings
        if direction == "L":
            
            # old method, only count when reaching exactly zero
            if not new_protocol and start_value == 0:
                exactly_zero += 1
            
            # new method, count zero and all zero crossings
            if new_protocol:
                number_of_wraps = abs((start_value - amount) // 100)
                wrap_arounds = wrap_arounds + number_of_wraps
                
        elif direction == "R":
            # old method, only count when reaching exactly zero
            if not new_protocol and start_value == 0:
                exactly_zero += 1
            
            # new method, count zero and all zero crossings
            if new_protocol:
                number_of_wraps = (start_value + amount) // 100
                wrap_arounds = wrap_arounds + number_of_wraps
        
        # Update starting position
        if direction == "L":
            start_value = (start_value - amount) % 100
        elif direction == "R":
            start_value = (start_value + amount) % 100
                
    if new_protocol:
        return wrap_arounds
    
    return exactly_zero


def part_one(data: str):
    ln = Utils.utils.lines(data)
    new_protocol = False
    value = apply_rotation(ln, new_protocol)
    return value

def part_two(data: str):
    ln = Utils.utils.lines(data)
    new_protocol = True
    value = apply_rotation(ln, new_protocol)
    return value

def main():
    # data = Utils.utils.read_input("Day01/test_input.txt")
    data = Utils.utils.read_input("Day01/real_input.txt")
    print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))

if __name__ == "__main__":
    main()
