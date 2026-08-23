from __future__ import annotations

from crystalline_zeta.geometry import (
    canonical_15_4_cells,
    continued_fraction,
    discrepancy,
    mechanical_word,
)


def main() -> None:
    p, q = 673, 1000
    word = mechanical_word(p, q, length=q)
    cells = canonical_15_4_cells()

    print(f"density = {sum(word)}/{len(word)} = {sum(word)/len(word):.12f}")
    print(f"continued fraction {p}/{q} = {continued_fraction(p, q)}")
    print(f"prefix discrepancy = {discrepancy(word, p, q):.12f}")
    print()
    print("canonical 19-cell defect supercell")
    print(f"cell lengths = {cells.cell_lengths}")
    print(f"long-cell indices = {cells.long_cell_indices}")
    print(f"long-cell cyclic spacings = {cells.long_cell_spacings()}")
    print(f"total encoded length = {cells.total_length}")


if __name__ == "__main__":
    main()
