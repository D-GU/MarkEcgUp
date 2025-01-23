import h5py
import matplotlib.pyplot as plt
from neurokit2.ecg import ecg_clean
from numpy import load

file_path = "/home/forest/Developer/Datasets/ptbxl/ecg_ptbxl.npy"
file = load(file_path)


def to_h5():
    with h5py.File("ptbxl.h5", "w") as f:
        for patient_id in range(file.shape[0]):  # Перебор всех пациентов
            patient_group = f.create_group(str(patient_id))  # Создаем группу для пациента
            for lead_id in range(file.shape[2]):  # Перебор всех отведений
                # Сохраняем данные отведения в dataset
                clean_ecg = ecg_clean(file[patient_id][:, lead_id], sampling_rate=100)
                patient_group.create_dataset(str(lead_id), data=clean_ecg)


with h5py.File("ptbxl.h5", "r") as f:
    # Доступ к данным пациента 200, отведения 5
    patient_id = "0"
    lead_id = "2"
    if patient_id in f and lead_id in f[patient_id]:
        lead_data = f[patient_id][lead_id][:]
        fgf = lead_data
        print(f"Данные пациента {patient_id}, отведение {lead_id}: {lead_data}")
        plt.plot(lead_data)
        plt.show()
