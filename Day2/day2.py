import pandas as pd

def find_position(startX, startY, l):
    '''
    Find the final horizontal and depth values after following the instructions in list 'l'
    Start positions are defined by startX and startY
    '''
    x = startX
    depth=startY
    for direction in l:
        instructions = direction[0].split(' ')
        if instructions[0] == 'forward':
            x += int(instructions[1])
        elif instructions[0] == 'up':
            depth -= int(instructions[1])
        elif instructions[0] == 'down':
            depth += int(instructions[1])
        else:
            print('Unrecognised direction')
            return 0

    return x, depth

def find_position_aim(startX, startAim, startDepth, l):
    '''
    Find the final horizontal and depth values with up and down affecting aim rather than depth
    '''
    horizontal = startX
    aim = startAim
    depth = startDepth
    for direction in l:
        instructions = direction[0].split(' ')
        if instructions[0] == 'forward':
            horizontal += int(instructions[1])
            depth += aim * int(instructions[1])
        elif instructions[0] == 'up':
            aim -= int(instructions[1])
        elif instructions[0] == 'down':
            aim += int(instructions[1])
        else:
            print('Unrecognised direction')
            return 0

    return horizontal, depth

    

if __name__ == '__main__':
    input = pd.read_csv('input.txt', header=None).values
    horizontal, depth = find_position(0,0,input)
    print('Part 1:')
    print(f'After those directions we are at horizontal {horizontal} and depth {depth}')
    print(f'The product of these is {horizontal * depth}')

    horizontal, depth = find_position_aim(0,0,0,input)

    print('Part 2:')
    print(f'After those directions we are at horizontal {horizontal} and depth {depth}')
    print(f'The product of these is {horizontal * depth}')