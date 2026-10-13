# Brainfuck Interpreter in Python

A lightweight **Brainfuck** esoteric programming language interpreter written in Python for an academic assignment.

## Features

- **Standard Memory Tape:** Default buffer of 30,000 cells.
- **8-Bit Wrapping:** Cells wrap automatically between `0` and `255` (modulo 256).
- **Efficient Loop Resolution:** Precomputes bracket jump targets (`[` and `]`) using a stack for $O(1)$ runtime jumps.
- **Immediate I/O:** ASCII character output with immediate stdout flushing and standard input reading.

## Instruction Set

| Command | Description |
|:-------:|:---|
| `>` | Moves the data pointer to the next cell |
| `<` | Moves the data pointer to the previous cell |
| `+` | Increments the byte at the data pointer (wraps from 255 to 0) |
| `-` | Decrements the byte at the data pointer (wraps from 0 to 255) |
| `.` | Outputs the byte at the data pointer as an ASCII character |
| `,` | Accepts one byte of input and stores its value in the current cell |
| `[` | Jumps forward past the matching `]` if the current cell is 0 |
| `]` | Jumps back to the matching `[` if the current cell is non-zero |

## Requirements & Usage

- **Python 3.8+** (no external dependencies required)

Run the script from your terminal:

```bash
python main.py
