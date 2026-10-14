"""
Step 2 - Clean the raw data and add analysis columns for Power BI.
Input : data/restaurants_raw.csv
Output: data/restaurants_clean.csv   <- this is the file you load in Power BI
"""
import pandas as pd

df = pd.read_csv("data/restaurants_raw.csv")
print("Raw rows:", len(df))

# 1. Fix inconsistent text (extra spaces / UPPERCASE)
for col in ["restaurant_name", "locality", "zone", "cuisine", "restaurant_type"]:
    df[col] = df[col].astype(str).str.strip().str.title()

# 2. Remove duplicates and rows with no rating
df = df.drop_duplicates(subset=["restaurant_id"])
df = df.dropna(subset=["rating"])

# 3. Correct data types
df["rating"] = df["rating"].astype(float)
df["avg_cost_for_two"] = df["avg_cost_for_two"].astype(int)
df["votes"] = df["votes"].astype(int)

# 4. Derived columns (these power the pricing / rating visuals)
df["price_band"] = pd.cut(
    df["avg_cost_for_two"],
    bins=[0, 500, 1000, 2000, 10000],
    labels=["1. Budget (<=500)", "2. Mid-range (501-1000)",
            "3. Premium (1001-2000)", "4. Luxury (>2000)"],
)
df["rating_band"] = pd.cut(
    df["rating"],
    bins=[0, 3.0, 3.5, 4.0, 5.0],
    labels=["1. Poor (<=3.0)", "2. Average (3.1-3.5)",
            "3. Good (3.6-4.0)", "4. Excellent (4.1+)"],
)
df["value_score"] = (df["rating"] / df["avg_cost_for_two"] * 1000).round(2)
df["restaurant_age"] = 2026 - df["opened_year"]

df.to_csv("data/restaurants_clean.csv", index=False)
print("Clean rows:", len(df))
print("Saved data/restaurants_clean.csv")
print(df.groupby("zone")[["rating", "avg_cost_for_two"]].mean().round(2))
