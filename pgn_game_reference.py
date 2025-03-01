#!/usr/bin/env python

import argparse
import chess.pgn


def parse_pgn(file_path, format_type):
    with open(file_path, "r", encoding="utf-8") as pgn_file:
        games = []
        while True:
            game = chess.pgn.read_game(pgn_file)
            if game is None:
                break  # End of file

            # Extract relevant PGN metadata
            white = game.headers.get("White", "Unknown")
            black = game.headers.get("Black", "Unknown")
            event = game.headers.get("Event", "Unknown Event")
            date = game.headers.get("Date", "????.??.??")
            year = date.split(".")[0] if date != "????.??.??" else "Unknown Year"
            result = game.headers.get("Result", "*")
            eco = game.headers.get("ECO", "Unknown ECO")
            round_num = game.headers.get("Round", "?")

            # Choose output format based on user selection
            if format_type == "standard":
                game_line = (
                    f"{white} - {black}, {year} ({event}), {result} [ECO: {eco}]"
                )
            elif format_type == "short":
                game_line = f"{white} - {black}, {year}, {result}"
            elif format_type == "full":
                game_line = (
                    f"{white} - {black}, {year} ({event}, Round {round_num}), {result}"
                )
            else:
                raise ValueError("Invalid format type.")

            games.append(game_line)

        return games


def main():
    parser = argparse.ArgumentParser(
        description="Extract one-line references from a PGN file. Default output format is 'standard'."
    )
    parser.add_argument("pgn_file", help="Path to the PGN file")
    parser.add_argument(
        "-f",
        "--format",
        choices=["standard", "short", "full"],
        default="standard",  # Explicitly set standard as the default
        help="Choose output format: 'standard' (default), 'short', or 'full'.",
    )

    args = parser.parse_args()
    games = parse_pgn(args.pgn_file, args.format)

    for game in games:
        print(game)


if __name__ == "__main__":
    main()
