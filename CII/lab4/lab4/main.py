import argparse

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main(path):
    data = pd.read_csv(path)
    print(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lab3 package")
    parser.add_argument(
        "-p", "--path",
        action="store",
        metavar="./data/Student_Performance.csv",
        help="data path",
        required=True,
    )
    parsed = parser.parse_args()
    data_path = parsed.path

    main(data_path)
