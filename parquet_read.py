import pandas as pd
import matplotlib.pyplot as plt

file_path = "NOTAG_merged.parquet"     # <-- change this


df = pd.read_parquet(file_path)
pd.set_option("display.max_columns", None)

for col in df.columns:
    print(col)

column_to_plot = "lead_pt"
if column_to_plot not in df.columns:
    raise ValueError(f"Column '{column_to_plot}' not found in dataset")

plt.figure()

if pd.api.types.is_numeric_dtype(df[column_to_plot]):
    df[column_to_plot].plot(kind="hist", bins=50)
    plt.ylabel("A. U.")

plt.title(f"{column_to_plot}")
plt.xlabel(column_to_plot)
plt.tight_layout()
plt.show()
