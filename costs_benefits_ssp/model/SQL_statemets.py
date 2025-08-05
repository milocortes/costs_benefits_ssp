from enum import Enum

class Statement(Enum):
    LVSTTLUConversion = "SELECT * FROM lvst_tlu_conversions"
    WALISanitationClassificationSP = "SELECT * FROM wali_sanitation_classification"

    