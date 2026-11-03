from pathlib import Path

# ==========================================
# PROJECT ROOT
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# ==========================================
# NFL DATA DIRECTORIES
# ==========================================

RAW_DATA_DIR = PROJECT_ROOT / "01_Raw_Data"
CLEAN_DATA_DIR = PROJECT_ROOT / "02_Clean_Data"

# ==========================================
# BDB 2026 DATA DIRECTORIES
# ==========================================

BDB_2026_DATA_DIR = PROJECT_ROOT / "01_BDB_2026_Data"

BDB_2026_BEFORE_PASS_DIR = (
    BDB_2026_DATA_DIR / "01_Before_Pass_Data"
)

BDB_2026_SUPPLEMENTARY_DIR = (
    BDB_2026_DATA_DIR / "03_Supplementary_Data"
)

# ==========================================
# WR SEPARATION ANALYSIS OUTPUTS
# ==========================================

SEPARATION_DATA_DIR = (
    PROJECT_ROOT / "05_WR_Separation_Analysis" / "Data"
)

SEPARATION_IMAGES_DIR = (
    PROJECT_ROOT / "05_WR_Separation_Analysis" / "Images"
)
