from .cmod import hello_from_bin, square_from_bin
from ._version import __version__

__all__ = ["hello", "square", "__version__"]


def hello() -> None:
    return hello_from_bin()


def square(n: float) -> float:
    return square_from_bin(n)
