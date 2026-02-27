"""Pokemon training module with batch training and summaries."""

from typing import List


class Pokemon:
    """Represents a Pokemon with a name and power level."""

    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    @property
    def level(self) -> int:
        """Derived level based on power."""
        return self.power // 5


def train(pokemon: Pokemon, sessions: int = 1) -> None:
    """Increase a Pokemon's power by training sessions."""
    pokemon.power += sessions


def batch_train(pokemons: List[Pokemon], sessions: int = 1) -> None:
    """Train a list of Pokemon."""
    for p in pokemons:
        train(p, sessions)


def summarize(pokemons: List[Pokemon]) -> None:
    """Print a summary of all Pokemon."""
    print("\nPokemon Summary")
    print("-" * 30)

    for p in pokemons:
        print(f"{p.name:<12} Power: {p.power:<3} Level: {p.level}")

    min_power = min(p.power for p in pokemons)
    max_power = max(p.power for p in pokemons)

    print("-" * 30)
    print(f"Min Power: {min_power} | Max Power: {max_power}")


if __name__ == "__main__":
    pokemons = [
        Pokemon("Pikachu", 5),
        Pokemon("Charmander", 7),
        Pokemon("Bulbasaur", 6),
        Pokemon("Squirtle", 4),
        Pokemon("Caterpie", 2),
        Pokemon("Steelix", 55), 
        Pokemon("Lugia", 70),
        Pokemon("Pidgey", 3),
        Pokemon("Stantler", 22)
    ]

    summarize(pokemons)
    batch_train(pokemons, sessions=3)
    summarize(pokemons)