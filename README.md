# SignalVelocity

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17596297.svg)](https://doi.org/10.5281/zenodo.17596297)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

SignalVelocity is a Python tool for creating **quiver ("velocity") plots** comparing two ChIP-seq (or similar) signal tracks over a **single genomic region of interest**.

The SignalVelocity workflow consists of the following steps:

1. Convert each bigWig signal track into a **binned bedGraph** file restricted to the genomic region of interest.
2. Use `signalvelocity` to process the two bedGraph files and generate:
   - a **PDF velocity plot** visualizing directional changes between conditions, and  
   - a corresponding **binned BED file** documenting the exact bins used.
3. (Optional, but recommended) Refine the PDF for presentation or publication using a vector-graphics editor such as [Inkscape](https://www.inkscape.org/).

Note: The visual appearance of the velocity plot (e.g., arrow density, bin size, scaling) often benefits from trial-and-error tuning.  
Different genomic regions and signal profiles may require slightly different parameter choices to achieve optimal readability.

---

## Repository layout

```
.
├── CITATION.cff
├── environment_minimal.yaml
├── environment.yaml
├── LICENSE
├── README.md
├── src
│   └── signalvelocity
│       ├── cli.py
│       └── core.py
└── tests
    ├── bws.lst
    ├── ExpectedOutput.Velocity_H3K4me3.binSize_50.bed
    ├── ExpectedOutput.Velocity_H3K4me3.VelocityPlot.pdf
    ├── H3K4me3_DMSO.bwc.bin_50.bdg
    ├── H3K4me3_ST1.bwc.bin_50.bdg
    └── regionOfInterest.bed
```

The `tests/` directory contains demo input files and expected outputs.

---

# STEP 0: Installation

## Step 0a: Pull repository and enter main directory

```
cd signalvelocity
```

## Step 0b: Set up the conda environment

```
conda env create -f environment_minimal.yaml
conda activate signalvelocity
```

## Step 0c: Add `src` to your `$PYTHONPATH`

```
export PYTHONPATH="$PWD/src:$PYTHONPATH"
```

This allows Python to locate the package when running the CLI via `python -m`.

---

# STEP 1: Prepare the input files

**Purpose:** Convert bigWig files into binned bedGraph files restricted to:

* a **single region**, and
* a **user-defined bin size**.

These bedGraph files are then used by `signalvelocity`.

## Step 1a: Create a list of bigWig files

Example `bws.lst`:

```
/absolute/path/to/file/H3K4me3_DMSO.bw
/absolute/path/to/file/H3K4me3_ST1.bw
```

If multiple replicates exist per condition, it is recommended to merge them before this step.

## Step 1b: Save the region of interest as a BED file

Example `regionOfInterest.bed`:

```
chr9	69035000	69039600
```

Only one region can be processed at a time.

## Step 1c: Convert bigWig to binned bedGraph

```
region=$(awk '{print $1":"$2":"$3}' regionOfInterest.bed)
bin=50
bws=bws.lst

while read -r bw; do
    [ -z "${bw}" ] && continue

    base=$(basename "${bw}")
    base=${base%.bw}

    outPrefix="${base}.bwc"

    time bigwigCompare \
        --bigwig1 "${bw}" \
        --bigwig2 "${bw}" \
        --operation mean \
        --binSize "${bin}" \
        --region "${region}" \
        --numberOfProcessors 1 \
        --outFileName "${outPrefix}.bin_${bin}.bdg" \
        --outFileFormat bedgraph &
done < ${bws}
```

### Typical processing time

A few seconds per bigWig (<1GB).

Note: Example `.bdg` files are included in `tests/`, but bigWigs are not.

---

# STEP 2: Generate SignalVelocity plots

To generate the velocity/quiver plot from two bedGraph files, run:

```
cd tests
python -m signalvelocity.cli \
  H3K4me3_DMSO.bwc.bin_50.bdg \
  H3K4me3_ST1.bwc.bin_50.bdg \
  --binSize 50 \
  --layers 5 \
  --width 0.017 \
  --scale 6 \
  --yMax 2.5 \
  --regionsBedFile regionOfInterest.bed \
  --outfilePrefix ExpectedOutput.SignalVelocity_H3K4me3
```

This will generate:

* `ExpectedOutput.SignalVelocity_H3K4me3.binSize_50.bed`
* `ExpectedOutput.SignalVelocity_H3K4me3.VelocityPlot.pdf`

### Typical processing time

Just a few seconds.

---

## Troubleshooting

**Module not found** -> Ensure:

```
export PYTHONPATH="$PWD/src:$PYTHONPATH"
conda activate signalvelocity
```

**Missing deepTools** -> Install or add `bigwigCompare` to PATH.

**Empty plots** -> Confirm:

* Region BED matches genome
* Bin size in Step 1c matches `--binSize`
* bedGraphs contain data for the region

---

## License
This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

## Citation
If you use SignalVelocity in your research, please cite the archived release:

**Rosikiewicz W. SignalVelocity (v0.2.0). Zenodo. https://doi.org/10.5281/zenodo.17596297**

