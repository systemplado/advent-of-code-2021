from typing import Tuple


class PartOne():
    def move_coordinates(position: Tuple[int, int], move: Tuple[str, int]) -> Tuple[int, int]:
        """
        returns a Tuple[int, int] of (x,y) coordinates

        position: current (x,y) position
        move: move by (direction, units)
            direction: "forward" -> x + units
            direction: "up" -> y - units
            direction: "down" -> y + units
        """
        direction = move[0]
        units = move[1]

        x = position[0]
        y = position[1]

        if direction == "forward":
            return (x + units, y)
        elif direction == "up":
            return (x, y - units)
        elif direction == "down":
            return (x, y + units)

        return position

    def get_final_position(position: Tuple[int, int]) -> int:
        return position[0] * position[1]


class PartTwo():
    def move_coordinates(position: Tuple[int, int, int], move: Tuple[str, int]) -> Tuple[int, int, int]:
        """
        returns a Tuple[int, int] of (x,y) coordinates

        position: current (x,y, aim) position
        move: move by (direction, units)
            direction: "forward" -> x + units, y + (aim * units)
            direction: "up" -> aim - units
            direction: "down" -> aim + units
        """
        direction = move[0]
        units = move[1]

        x = position[0]
        y = position[1]
        aim = position[2]

        if direction == "forward":
            return (x + units, y + (aim * units), aim)
        elif direction == "up":
            return (x, y, aim - units)
        elif direction == "down":
            return (x, y, aim + units)

        return position

    def get_final_position(position: Tuple[int, int, int]) -> int:
        return position[0] * position[1]
