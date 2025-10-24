# Configuration file with all settings
import os

# Base directories
BASE_DIR = os.path.dirname(__file__)             # directory of config.py
NETCDF_FILE = os.path.join(BASE_DIR, "data")

REFLECTANCE_VAR = 'reflectance'
TIME_DIM = 'time'
LAT_DIM = 'lat'
LON_DIM = 'lon'
WAVELENGTH_DIM = ['412', '443', '490', '510', '555', '670']

OUTPUT_DIR = 'outputs/'
FIGURE_DIR = 'outputs/figures/'
CSV_DIR = os.path.join(BASE_DIR, "outputs/csv")