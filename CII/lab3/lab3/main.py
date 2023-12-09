import argparse
from lab3.pl.pl import PrologWorker


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lab3 package")
    parser.add_argument(
        "-s", "--script",
        action="store",
        metavar="../lab1/rules.pl",
        help="script path",
        required=True,
    )
    parsed = parser.parse_args()
    script_path = parsed.script

    pl = PrologWorker(path=script_path)
    pl.run()
