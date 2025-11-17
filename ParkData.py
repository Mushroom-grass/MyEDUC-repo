import pandas as pd

file_path = "/Users/yuanqihu/Library/CloudStorage/OneDrive-PennO365/2025Fall/EDUC5913/MyEDUC-repo/Acreage_Park_System_Highlights_WEB_DATA_TABLES_City_Park_Facts_2025.xlsx"


# --------- 各表清洗函数 ---------

def load_most_visited(path):
    raw = pd.read_excel(path, sheet_name="Most Visited Parks", header=2)
    header = raw.iloc[0]
    df = raw.iloc[1:].copy()
    df.columns = header
    df = df[['FIPS', 'City name', 'Park Name', 'Annual Visitation']]
    df.rename(columns={
        'City name': 'City',
        'Park Name': 'MostVisited_Park',
        'Annual Visitation': 'Annual_Visitation'
    }, inplace=True)
    df['Annual_Visitation'] = pd.to_numeric(df['Annual_Visitation'], errors='coerce')
    return df


def load_largest_parks(path):
    raw = pd.read_excel(path, sheet_name="Largest Parks", header=2)
    header = raw.iloc[0]
    df = raw.iloc[1:].copy()
    df.columns = header
    df = df[['FIPS', 'City name', 'Park Name', 'Park Size (Acres)']]
    df.rename(columns={
        'City name': 'City',
        'Park Name': 'Largest_Park',
        'Park Size (Acres)': 'Largest_Park_Acres'
    }, inplace=True)
    df['Largest_Park_Acres'] = pd.to_numeric(df['Largest_Park_Acres'], errors='coerce')
    return df


def load_oldest_parks(path):
    raw = pd.read_excel(path, sheet_name="Oldest Parks", header=2)
    header = raw.iloc[0]
    df = raw.iloc[1:].copy()
    df.columns = header
    df = df[['FIPS', 'City name', 'Park Name', 'Year Established']]
    df.rename(columns={
        'City name': 'City',
        'Park Name': 'Oldest_Park',
        'Year Established': 'Year_Established'
    }, inplace=True)
    df['Year_Established'] = pd.to_numeric(df['Year_Established'], errors='coerce')
    return df


def load_city_population(path):
    raw = pd.read_excel(path, sheet_name="City Population Statistics", header=4)
    header = raw.iloc[0]
    df = raw.iloc[1:].copy()
    df.columns = header
    df = df[['FIPS', 'City Name', 'Population']]
    df.rename(columns={'City Name': 'City'}, inplace=True)
    df['Population'] = pd.to_numeric(df['Population'], errors='coerce')
    return df


# --------- 载入四个表 ---------

most_df = load_most_visited(file_path)
largest_df = load_largest_parks(file_path)
oldest_df = load_oldest_parks(file_path)
pop_df = load_city_population(file_path)

# --------- 合并 ---------

merged = (
    most_df
    .merge(largest_df[['FIPS', 'Largest_Park_Acres']], on='FIPS', how='left')
    .merge(oldest_df[['FIPS', 'Year_Established']], on='FIPS', how='left')
    .merge(pop_df[['FIPS', 'Population']], on='FIPS', how='left')
)

print("\n==== 合并后数据示例 ====")
print(merged.head())

# --------- 相关性分析（不用画图） ---------

numeric_cols = ['Annual_Visitation', 'Largest_Park_Acres', 'Year_Established', 'Population']
corr = merged[numeric_cols].corr()

print("\n==== 数值列的相关性矩阵 ====")
print(corr)

# --------- 用文字解释关系 ---------

def explain_corr(c):
    if c > 0.6:
        return "强正相关（数值一起上升）"
    elif 0.3 < c <= 0.6:
        return "中度正相关"
    elif 0.1 < c <= 0.3:
        return "弱正相关"
    elif -0.1 <= c <= 0.1:
        return "几乎无相关"
    elif -0.3 <= c < -0.1:
        return "弱负相关"
    elif -0.6 <= c < -0.3:
        return "中度负相关"
    else:
        return "强负相关（一个上升一个下降）"


print("\n==== 简单文字说明 ====\n")

for col in ['Largest_Park_Acres', 'Year_Established', 'Population']:
    c = corr.loc['Annual_Visitation', col]
    print(f"Most visited park 的访问量 vs {col} 的相关性：{c:.2f} → {explain_corr(c)}")
