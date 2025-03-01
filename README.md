# PGN One-Line Game Reference Extractor

This script extracts one-line game references from a Portable Game Notation (PGN) file and formats them in a concise manner. It supports multiple output formats used in chess databases, literature, and reports.

## Features
- Parses PGN files to extract key game metadata.
- Supports three output formats:
  - **Standard (default)**: `White - Black, Year (Event), Result [ECO: Code]`
  - **Short**: `White - Black, Year, Result`
  - **Full (with Round Number)**: `White - Black, Year (Event, Round X), Result`
- Command-line interface with `argparse` for flexibility.

## Installation
Ensure you have Python installed (version 3.x recommended).  
You'll need the `python-chess` library, which can be installed with:

```sh
pip install -r requirements.txt
```

## Usage

### Basic Usage (Standard Format)
To extract one-line game references using the **default standard format**:

```sh
python pgn_game_reference.py games.pgn
```

### Specifying Output Format
Use the `-f` or `--format` option to choose a format:

- **Standard Format (default)**
  ```sh
  python pgn_game_reference.py games.pgn
  ```
  **Output:**
  ```
  Magnus Carlsen - Fabiano Caruana, 2018 (World Championship Match), 1/2-1/2 [ECO: B30]
  ```

- **Short Format**
  ```sh
  python pgn_game_reference.py games.pgn -f short
  ```
  **Output:**
  ```
  Kasparov - Karpov, 1985, 1-0
  ```

- **Full Format (Includes Round)**
  ```sh
  python pgn_game_reference.py games.pgn --format full
  ```
  **Output:**
  ```
  Anand - Topalov, 2010 (World Championship, Round 4), 1-0
  ```

## Arguments
| Argument | Short | Description |
|----------|-------|-------------|
| `pgn_file` | (positional) | Path to the PGN file. |
| `--format` | `-f` | Choose output format: `standard` (default), `short`, or `full`. |

## Example PGN File
A simple example of a PGN game that this script can process:

```pgn
[Event "World Chess Championship"]
[Site "London, UK"]
[Date "2018.11.09"]
[Round "1"]
[White "Magnus Carlsen"]
[Black "Fabiano Caruana"]
[Result "1/2-1/2"]
[ECO "B30"]

1. e4 c5 2. Nf3 Nc6 3. Bb5 g6 4. Bxc6 dxc6 5. d3 Bg7 6. h3 e5 7. Be3 b6 8. a4 ...
```

## Notes
- The script automatically detects and formats all games inside the PGN file.
- If a tag is missing in the PGN file, a placeholder such as `"Unknown"` will be used.

## License
This script is provided **without a license** and is free to use, modify, and distribute without restrictions.

---

### Contributions
Contributions are welcome! Feel free to fork, modify, or suggest improvements.

### Contact
For questions or suggestions, feel free to open an issue or contact the author.
