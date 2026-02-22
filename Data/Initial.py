import kagglehub
import shutil
import os

target_dir = r"G:\Project\SuperStore-Analyse\Data"

path = kagglehub.dataset_download("vivek468/superstore-dataset-final")

shutil.copytree(path, target_dir, dirs_exist_ok=True)

print("Dataset saved to:", target_dir)