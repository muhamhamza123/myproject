import subprocess
for nb in ["SE1_data_access.ipynb","SE2_data_processing.ipynb","SE3_model_train_validate.ipynb","SE4_generate_outputs.ipynb"]:
    subprocess.run(f"jupyter nbconvert --execute --to notebook --inplace notebooks/{nb}", shell=True, check=True)
print("Workflow complete")
