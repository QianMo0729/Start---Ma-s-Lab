import pandas as pd

url = "/Users/mason/Desktop/Ma's Lab/Getting Start/Dataset/salaries.csv"
raw = pd.read_csv(url)

print("数据规模：", raw.shape)
print(raw.head())
raw.info()

data = raw.copy()
data.columns = data.columns.str.strip()

for col in data.select_dtypes(include=["object", "string"]).columns:
    data[col] = data[col].str.strip().replace("", pd.NA)

data["salary_in_usd"] = pd.to_numeric(
    data["salary_in_usd"], errors="coerce"
)

print("\n各列缺失值：")
print(data.isna().sum())

print("\n完全相同的额外行数：", data.duplicated().sum())

invalid_salary = (
    data["salary_in_usd"].isna()
    | data["salary_in_usd"].le(0)
)
print("无法用于薪资分析的行数：", invalid_salary.sum())

clean = data.loc[~invalid_salary].copy()

print("\n美元薪资描述统计：")
print(clean["salary_in_usd"].describe().round(2))

print("\n记录数最多的 5 个岗位：")
print(clean["job_title"].value_counts().head(5))

print("\n按经验等级统计薪资：")
print(
    clean.groupby("experience_level")["salary_in_usd"]
    .agg(["count", "mean", "median"])
    .reindex(["EN", "MI", "SE", "EX"])
    .round(2)
)

print("\n公司所在地区占比（前 5）：")
print(
    clean["company_location"]
    .value_counts(normalize=True)
    .head(5)
    .mul(100)
    .round(2)
)