# NFL Big Data Bowl 2027: Combine to NFL Performance

## Project Overview

This project investigates whether movement characteristics measured during the NFL Scouting Combine are associated with on-field performance in the NFL.

Using 10 Hz Combine tracking data and NFL game tracking data, the analysis develops position-specific acceleration and deceleration metrics to identify movement abilities that may not be captured by traditional Combine testing. The goal is to uncover actionable relationships between athletic testing and in-game performance that can help coaches and scouts better evaluate prospects.

The analysis focuses on wide receivers (WRs) and defensive backs (DBs), examining how acceleration and deceleration relate to separation during different route types.

## Key Findings

The analysis identifies three primary relationships:

1. **Wide receiver deceleration and cutting routes:** WR deceleration ability is associated with creating separation on cutting routes, including hitch, in, and out routes.
2. **Wide receiver acceleration and burst routes:** WR acceleration ability is associated with generating separation on burst routes, including go, post, and corner routes.
3. **Defensive back deceleration and cutting routes:** DB deceleration ability is associated with limiting the separation WRs generate on cutting routes.

These findings suggest that acceleration and deceleration characteristics derived from Combine tracking data may provide additional scouting information beyond traditional Combine metrics.

A central application is identifying potential undervalued prospects whose movement characteristics compare favorably with their overall athleticism evaluations. These metrics may also help inform position-specific training and development.

*The findings represent statistical associations and should not be interpreted as evidence of causation.*

## Repository Structure

| Directory | Description |
|---|---|
| `04_EDA/` | Exploratory data analysis and preliminary investigations |
| `05_WR_Separation_Analysis/` | Combine movement feature development, WR/DB matching, route analysis, and performance modeling |
| `05_WR_Separation_Analysis/Analysis/` | Analysis outputs and comparison tables |
| `05_WR_Separation_Analysis/Images/` | Figures and visualizations used throughout the analysis |
| `05_WR_Separation_Analysis/Data_Pull/` | Data selection and analysis parameters |
| `utils/` | Shared project utilities, including data schemas and path configuration |

Raw NFL datasets, cleaned datasets, and intermediate analysis data are not included in this repository.

## Environment Setup

This project uses Python 3.12 and [`uv`](https://docs.astral.sh/uv/) for dependency management.

### 1. Clone the repository

```bash
git clone <repository-url>
cd Big-Data-Bowl-2027
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Activate the environment

```bash
source .venv/bin/activate
```

### 4. Launch Jupyter

```bash
uv run jupyter lab
```

The project dependencies and exact package versions are maintained in `pyproject.toml` and `uv.lock`.

## Reproducing the Analysis

The NFL datasets required to run the notebooks are not distributed with this repository. Users must obtain the appropriate datasets and place them in the expected local data directories.

The project uses shared schemas in `utils/schema.py` and centralized directory definitions in `utils/paths.py` to manage data access across notebooks.

### R Markdown Figures

The top-five player comparison tables are generated using R Markdown. Reproducing these figures requires:

- R
- The R packages `rmarkdown`, `tidyverse`, `gt`, and `nflreadr`
- [Pandoc](https://pandoc.org/)

On macOS, Pandoc can be installed with:

```bash
brew install pandoc
```

The comparison-table CSV inputs are maintained in `05_WR_Separation_Analysis/Analysis/`.

## Author

NFL Big Data Bowl 2027 submission project.