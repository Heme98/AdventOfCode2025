import Utils.utils



def apply_rotation(rotation: list[str], new_method: bool) -> int:
    wrap_arounds = 0
    exactly_zero = 0
    start_value = 50
    
    for r in rotation:
        direction, amount = r[0], int(r[1:])
        
        # Calculate zero crossings
        if direction == "L":
            
            # old method, only count when reaching exactly zero
            if not new_method and start_value == 0:
                exactly_zero += 1
            
            # new method, count zero and all zero crossings
            if new_method:
                # number_of_wraps = abs((start_value - amount) // 100)
                # wrap_arounds = wrap_arounds + number_of_wraps
                if start_value > 0 and amount >= start_value:
                    wrap_arounds += 1 + (amount - start_value) // 100
                elif start_value == 0 and amount >= 100:
                    # Starting from 0, we hit it again after 100 steps, then every 100 steps
                    wrap_arounds += amount // 100
                
        elif direction == "R":
            
            # old method, only count when reaching exactly zero
            if not new_method and start_value == 0:
                exactly_zero += 1
            
            # new method, count zero and all zero crossings
            if new_method:
                # number_of_wraps = (start_value + amount) // 100
                # wrap_arounds = wrap_arounds + number_of_wraps
                if start_value > 0:
                    steps_to_zero = 100 - start_value
                if amount >= steps_to_zero:
                    wrap_arounds += 1 + (amount - steps_to_zero) // 100
                else:  # position == 0
                    # Starting from 0, we hit it again after 100 steps, then every 100 steps
                    if amount >= 100:
                        wrap_arounds += amount // 100
        
        # Update start_value
        if direction == "L":
            start_value = (start_value - amount) % 100
        elif direction == "R":
            start_value = (start_value + amount) % 100
        
                        
    if new_method:
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
