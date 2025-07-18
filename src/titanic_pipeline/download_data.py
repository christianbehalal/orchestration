import seaborn as sns

df = sns.load_dataset("titanic")
from pathlib import Path

data_dir = Path(__file__).resolve().parents[2] / "data" / "01_raw"
data_dir.mkdir(parents=True, exist_ok=True)
df.to_csv(data_dir / "titanic.csv", index=False)
print(f"✅ Dataset Titanic sauvegardé dans {data_dir / 'titanic.csv'}")


print("✅ Dataset Titanic sauvegardé dans data/01_raw/titanic.csv")
