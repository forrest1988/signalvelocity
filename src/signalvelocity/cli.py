# src/velocityplot/cli.py
import argparse
from .core import plotVelocity

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Create a velocity (quiver) plot from two BDG files."
    )
    p.add_argument("input1", help="BDG file for condition 1")
    p.add_argument("input2", help="BDG file for condition 2")
    p.add_argument("--binSize", type=int, required=True)
    p.add_argument("--layers", type=int, default=5)
    p.add_argument("--width", type=float, default=0.017)
    p.add_argument("--scale", type=float, default=6)
    p.add_argument("--yMax", type=float, default=2.5)
    p.add_argument("--regionsBedFile", required=True)
    p.add_argument("--outfilePrefix", required=True)
    return p

def main(argv=None):
    """Entry point called as ``python -m velocityplot.cli`` or by the console‑script."""
    parser = _build_parser()
    ns = parser.parse_args(argv)

    # Build the filenames exactly the way you did in the notebook
    input1 = ns.input1
    input2 = ns.input2
    binSize = ns.binSize
    layers = ns.layers
    width = ns.width
    scale = ns.scale
    yMax = ns.yMax
    outfilePrefix = ns.outfilePrefix

    plotVelocity(
        input1, input2,
        binSize,
        outfilePrefix,
        ns.regionsBedFile,
        layers,
        width,
        scale,
        yMax
    )

if __name__ == "__main__":
    main()
