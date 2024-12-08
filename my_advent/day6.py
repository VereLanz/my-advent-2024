from pathlib import Path

import numpy as np

from my_advent import get_todays_puzzle

DIRECTION_MAP = {
    "^": complex(0, 1),
    "v": complex(0, -1),
    ">": complex(1, 0),
    "<": complex(-1, 0),
}
ROTATE_MARKER_MAP = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}


class Guard:
    def __init__(self, x_pos: int, y_pos: int, direction_marker: str):
        self.pos = complex(x_pos, y_pos)
        self.direction = DIRECTION_MAP[direction_marker]
            
    @property
    def current_coords(self) -> tuple[int, int]:
        # gives mathematical y,x -> np array input in this layout
        return (int(self.pos.imag), int(self.pos.real))
    
    @property
    def coords_in_front(self) -> tuple[int, int]:
        in_front = self.pos + self.direction
        # gives mathematical y,x -> np array input in this layout
        return (int(in_front.imag), int(in_front.real))
    
    def take_step(self):
        self.pos += self.direction
    
    def turn_right(self):
        self.direction *= complex(0, 1)
    

def set_starting_guard(spots: np.ndarray) -> Guard:
    for marker in DIRECTION_MAP.keys():
        start = np.where(spots == marker)
        if start[0].any():
            # rotate marker for guard to reflect rotatet input for numpy coords
            return Guard(start[1].item(), start[0].item(), ROTATE_MARKER_MAP[marker])
    raise ValueError(
        f"No starting marker was found! Looking for: {DIRECTION_MAP.keys()}"
    )


def calculate_guard_visited_spots(inputs: list[str]) -> int:
    spots = np.array([[spot for spot in line] for line in inputs])
    # rotate map AND start direction to keep coordinate system as intended
    # input 0,0 is "left lower corner", np 0,0 is "upper left", (y, x)!
    spots = np.rot90(spots, -1)
    guard = set_starting_guard(spots)
    spots[guard.current_coords] = "x"
    
    # walk the guard and set visited space 'x' until Index is out of bounds (= leaving)
    while True:
        try:
            # negative coord would wrap around, but we don't want that here
            if any(coord < 0 for coord in guard.coords_in_front):
                raise IndexError("Negative coordinates are not accepted here.")
            if spots[guard.coords_in_front] == "#":
                guard.turn_right()
            guard.take_step()
            spots[guard.current_coords] = "x"
        except IndexError:
            print("The guard has left the premises...")
            break
    
    return len(np.where(spots == "x")[0])


def b(inputs: list[str]) -> int:
    return len(inputs)


# only for least effort template working each day
a = calculate_guard_visited_spots
b = b


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)

    # my_puzzle.submit_a(a(my_puzzle.input_lines))
    # my_puzzle.submit_b(b(my_puzzle.input_lines))
