import subprocess
import sys

def mappointformat(point):
    return f"U+{point.upper()}"

def transform_range(s):
    splitted = s.split("-")
    if len(splitted) == 1:
        return mappointformat(splitted[0])
    elif len(splitted) == 2:
        return f"{mappointformat(splitted[0])}-{mappointformat(splitted[1])}"

if __name__ == "__main__":
    # FONT = "Symbols-2048-em Nerd Font Complete.ttf"
    FONT = sys.argv[1]
    # fc-query outputs a sorted space separated list. ie:
    # 23fb-23fe 2665 26a1 2b58 e000-e00a
    cp = subprocess.run(["fc-query", "--format=%{charset}", FONT], text=True, capture_output=True)
    transformed = (transform_range(s) for s in cp.stdout.split(" "))
    cp = subprocess.run(["fc-query", "--format=%{family}", FONT], text=True, capture_output=True)
    print("symbol_map {} {}".format(",".join(transformed), cp.stdout))
