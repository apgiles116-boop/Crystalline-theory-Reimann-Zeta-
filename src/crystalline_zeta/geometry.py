from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import floor
from typing import Iterable, List, Sequence, Tuple


def continued_fraction(p: int, q: int) -> list[int]:
    """Return the finite simple continued fraction of p/q."""
    if q == 0:
        raise ZeroDivisionError("q must be nonzero")
    out: list[int] = []
    a, b = p, q
    while b:
        k = a // b
        out.append(k)
        a, b = b, a - k * b
    return out


def mechanical_word(p: int, q: int, length: int | None = None, phase: int = 0) -> list[int]:
    """Lower mechanical word of slope p/q.

    Returns bits w_n = floor((n+1)p/q + phase/q) - floor(np/q + phase/q).
    For gcd(p,q)=1 and length=q this is a balanced Christoffel/Sturmian period
    with exactly p ones.
    """
    if not (0 <= p <= q):
        raise ValueError("require 0 <= p <= q")
    if q <= 0:
        raise ValueError("q must be positive")
    if length is None:
        length = q
    return [
        floor(((n + 1) * p + phase) / q) - floor((n * p + phase) / q)
        for n in range(length)
    ]


def run_lengths(bits: Sequence[int], symbol: int = 1) -> list[int]:
    """Lengths of consecutive runs of `symbol` in a linear binary word."""
    runs: list[int] = []
    cur = 0
    for b in bits:
        if b == symbol:
            cur += 1
        elif cur:
            runs.append(cur)
            cur = 0
    if cur:
        runs.append(cur)
    return runs


def positions(bits: Sequence[int], symbol: int = 1) -> list[int]:
    return [i for i, b in enumerate(bits) if b == symbol]


def cyclic_spacings(pos: Sequence[int], period: int) -> list[int]:
    if not pos:
        return []
    xs = sorted(x % period for x in pos)
    return [((xs[(i + 1) % len(xs)] - xs[i]) % period) for i in range(len(xs))]


def discrepancy(bits: Sequence[int], p: int, q: int) -> float:
    """Maximum prefix discrepancy from density p/q."""
    target = Fraction(p, q)
    s = 0
    best = Fraction(0, 1)
    for n, b in enumerate(bits, start=1):
        s += b
        d = abs(Fraction(s, 1) - n * target)
        if d > best:
            best = d
    return float(best)


@dataclass(frozen=True)
class DefectCellPattern:
    cell_lengths: tuple[int, ...]
    long_cell_indices: tuple[int, ...]

    @property
    def total_length(self) -> int:
        return sum(self.cell_lengths)

    def long_cell_spacings(self) -> list[int]:
        return cyclic_spacings(self.long_cell_indices, len(self.cell_lengths))


def defect_cells_from_binary_word(
    word: Sequence[int], short_cell: int = 35, long_cell: int = 37
) -> DefectCellPattern:
    """Interpret 0/1 as short/long defect cells."""
    cells = tuple(long_cell if b else short_cell for b in word)
    longs = tuple(i for i, b in enumerate(word) if b)
    return DefectCellPattern(cells, longs)


def canonical_15_4_cells() -> DefectCellPattern:
    """Balanced 19-cell pattern with 4 long cells.

    Mechanical words of slope 4/19 generate the 5,5,5,4 cyclic spacing pattern
    up to rotation, matching the observed defect-cell decomposition.
    """
    word = mechanical_word(4, 19, length=19)
    return defect_cells_from_binary_word(word, 35, 37)
