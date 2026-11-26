import os

SIGN = "NO TAILGATING \u2014 the ghost slipped in behind an intern in 2019 and still has badge access."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SIGN)


if __name__ == "__main__":
    main()
