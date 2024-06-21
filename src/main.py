from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum
from typing import Optional


PieceType = StrEnum("PieceType", ["KING", "ROOK", "BISHOP", "GOLD",
                                  "SILVER", "KNIGHT", "LANCE", "PAWN"])

Color = StrEnum("Color", ["SENTE", "GOTE"])  # BLACK, WHITE. sente goes first


@dataclass(frozen=True)
class Board:
    """
    manages game state and logic of moving/spawning/capturing pieces.
    essentially the logic kernel of the game, pure state encapsulated
    """
    pieces: dict[Pos, Piece] = {}

    def spawn_piece(self, piece: Piece, pos: Pos) -> Optional[Board]:
        pass

    def move_piece(self, piece: Piece, new_pos: Pos) -> Optional[Board]:
        pass

    def capture_piece(self, pos: Pos) -> Optional[Board]:
        pass


@dataclass(frozen=True)
class Piece:
    type: PieceType
    color: Color
    is_promoted: bool = False


@dataclass(frozen=True)
class Pos:
    row: int
    col: int


if __name__ == "__main__":
    print("hello world!")
