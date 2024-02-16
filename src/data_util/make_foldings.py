import argparse
import pickle
from time import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--structure_path", help="Path to .dot file containing structure predictions"
    )
    parser.add_argument(
        "--save_path",
        help="Where to save the transformed foldings, needed to run the model",
    )
    args = parser.parse_args()

    t0 = time()

    formatted = {}
    with open(args.structure_path, "r") as f:
        lines = f.readlines()
        print(f"Lines: {len(lines)} -> {len(lines)/3} RNAs")
        for i in range(0, len(lines), 3):
            sequence = lines[i + 1].strip().replace("U", "T").upper()
            struc_info = lines[i + 2].split(" ")
            structure = struc_info[0]
            score = float(struc_info[-1].strip().replace("(", "").replace(")", ""))
            formatted[sequence] = [structure, score]
            if i == 0:
                print(formatted)

    print(f"Dict created for {len(formatted)} RNAs")

    with open(args.save_path, "wb") as f:
        pickle.dump(formatted, f)

    print(time() - t0)


if __name__ == "__main__":
    main()
