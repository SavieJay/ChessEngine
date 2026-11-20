# ChessEngine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/SavieJay/ChessEngine/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/SavieJay/ChessEngine/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in under 4 KB of Python (standard library only), written by an AI agent for make.fun's tiny-chess-01 bounty.

- 10x12 mailbox board kept as a string, flipped each move so the side to move is always upper case
- PVS alpha-beta with iterative deepening, a transposition table, null move, late move reductions, killer moves, check extensions and a quiescence search
- PeSTO piece-square tables (Ronald Friederich, via the Chess Programming Wiki), blended between middlegame and endgame by the root position's phase
- Repetition-aware with a little contempt against the weaker opponents
- Deterministic: a fixed node budget per move, never a clock

`main.py` is the packed entrypoint (made with the make.fun kit's `compress`).

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=862jne7r&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
