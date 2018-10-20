import Generation.Generate
import numpy as np


def main():
    generator = Generation.Generate.Generate()
    gameboard = generator.generate_all_ships_positions()
    print(np.matrix(gameboard))


if __name__ == "__main__":
    main()