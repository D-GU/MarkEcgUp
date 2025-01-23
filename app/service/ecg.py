import os

import h5py
import numpy as np
from dotenv import load_dotenv
from pydantic.fields import Field

load_dotenv()

PATH = os.getenv("ECG_FILE_PATH")


def get_patient_by_id(ecg_id: int = Field(ge=0, le=21430)):
    patient_ecg = []

    with h5py.File(PATH, "r") as f:
        for lead in range(12):
            patient_ecg.append(f[str(ecg_id)][str(lead)][:])
        return np.array(patient_ecg)


if __name__ == "__main__":
    s = get_patient_by_id(1)
