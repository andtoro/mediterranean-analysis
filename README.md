# Mediterranean Sea Reflectance Analysis

Satellite reflectance data analysis for the Mediterranean Sea using Python.

## Project Structure
```
mediterranean_analysis/
|-- notebooks/		  # Jupyter notebooks
├── src/                  # Source code modules
├── data/                 # Data files (not tracked)
├── outputs/              # Analysis outputs (not tracked)
├── main.py               # Main analysis script
├── config.py             # Configuration settings
└── requirements.txt      # Python dependencies
```

## Setup

1. Clone the repository
2. Create virtual environment: `python3 -m venv venv`
3. Activate: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Usage
```bash
python main.py
```

## Requirements

- Python 11.2+
- See `requirements.txt` for package dependencies
# Mediterranean Analysis

This project analyzes satellite-based sea surface reflectance data collected over the last 20 years across the Mediterranean region.  
The main objective is to study long-term patterns, visualize temporal and spatial variations, and compare the satellite observations with modelled outputs from an ocean model provided by the National Institute of Geophysics and Oceanography (INGV).

---

## Project Overview

The analysis focuses on:
- Processing and cleaning satellite reflectance datasets.
- Computing temporal and spatial statistics over defined regions of interest.
- Visualizing trends and anomalies.
- Comparing satellite-derived values against corresponding outputs from the INGV ocean model.

---

## Repository Structure

mediterranean_analysis/
├── src/ # Source code modules (data loading, processing, visualization)
├── data/ # Raw and intermediate datasets (not tracked in Git)
├── outputs/ # Analysis results and generated figures (not tracked in Git)
├── notebooks/ # Jupyter notebooks for exploratory analysis and testing
├── main.py # Main entry point for running the analysis pipeline
├── config.py # Configuration settings and paths
├── requirements.txt # Python dependencies
└── README.md # Project documentation (this file)


---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mediterranean_analysis.git
   cd mediterranean_analysis

    Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Usage

To run the full analysis pipeline:

python main.py

Alternatively, you can explore individual components or visualize results interactively using the Jupyter notebooks in the notebooks/ folder.
Data Sources

    Satellite data: Sea surface reflectance products spanning approximately 20 years.

    Model data: Ocean model outputs provided by the National Institute of Geophysics and Oceanography (OGS), used for comparison and validation.

Outputs

The generated outputs (plots, maps, statistical summaries) are stored in the outputs/ directory.
These include:

    Time series of reflectance indices.

    Seasonal and interannual variability plots.

    Comparison plots between observed and modelled data.

Notes

    Large datasets are excluded from version control (data/ and outputs/ are listed in .gitignore).

    The project is modular: all processing and visualization functions are defined in src/.

    Configuration (file paths, parameters, variable names) is centralized in config.py.

License

This project is distributed under the MIT License.
See the LICENSE

file for more information.
Acknowledgements

Special thanks to the National Institute of Geophysics and Oceanography (OGS) for providing model data and technical support.
