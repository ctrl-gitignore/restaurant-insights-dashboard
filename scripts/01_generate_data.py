"""
Step 1 - Generate a SAMPLE (synthetic) Mumbai restaurant dataset.

NOTE: This data is simulated for learning/portfolio purposes. It is NOT scraped
from Zomato/Swiggy. If you have a real dataset (e.g. from Kaggle), skip this
script and put your CSV in data/restaurants_raw.csv with the same column names
(or edit 02_clean_data.py to match your columns).
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 1500

# locality: (zone, price multiplier, rating bias)
LOCALITIES = {
    "Colaba": ("South Mumbai", 1.35, 0.15),
    "Fort": ("South Mumbai", 1.10, 0.05),
    "Churchgate": ("South Mumbai", 1.10, 0.05),
    "Lower Parel": ("South Mumbai", 1.40, 0.10),
    "Bandra": ("Western Suburbs", 1.45, 0.15),
    "Juhu": ("Western Suburbs", 1.30, 0.05),
    "Andheri": ("Western Suburbs", 1.00, 0.00),
    "Goregaon": ("Western Suburbs", 0.90, -0.05),
    "Malad": ("Western Suburbs", 0.85, -0.05),
    "Borivali": ("Western Suburbs", 0.75, -0.10),
    "Dadar": ("Central Mumbai", 0.90, 0.05),
    "Sion": ("Central Mumbai", 0.80, 0.00),
    "Kurla": ("Central Mumbai", 0.70, -0.15),
    "Ghatkopar": ("Central Mumbai", 0.80, -0.05),
    "Powai": ("Central Mumbai", 1.15, 0.10),
    "Chembur": ("Harbour", 0.90, 0.00),
    "Vashi": ("Navi Mumbai", 0.85, -0.05),
    "Thane": ("Thane", 0.80, -0.05),
}

# cuisine: price multiplier
CUISINES = {
    "North Indian": 1.0, "Chinese": 0.9, "Italian": 1.3, "South Indian": 0.6,
    "Street Food": 0.4, "Continental": 1.25, "Seafood": 1.3, "Mughlai": 1.1,
    "Biryani": 0.8, "Bakery & Desserts": 0.6, "Japanese & Asian": 1.6,
    "Fast Food": 0.5,
}

# restaurant type: (base cost for two, online delivery prob, table booking prob)
TYPES = {
    "Quick Bites": (300, 0.85, 0.02),
    "Casual Dining": (900, 0.70, 0.35),
    "Cafe": (650, 0.60, 0.15),
    "Fine Dining": (2200, 0.25, 0.85),
    "Bar & Lounge": (1600, 0.20, 0.70),
}
TYPE_WEIGHTS = [0.30, 0.34, 0.18, 0.09, 0.09]

PREFIX = ["Royal", "Spice", "Urban", "Golden", "Sea", "Hungry", "Tandoor", "Little",
          "Maharaja", "Coastal", "Bombay", "Fresh", "Smoky", "Grand", "Desi", "Moon"]
SUFFIX = ["Kitchen", "Bistro", "Darbar", "Cafe", "Junction", "House", "Treat",
          "Express", "Table", "Corner", "Palace", "Grill", "Tadka", "Hub"]

loc_names = list(LOCALITIES)
cuis_names = list(CUISINES)
type_names = list(TYPES)

rows = []
for i in range(N):
    loc = rng.choice(loc_names)
    zone, p_mult, r_bias = LOCALITIES[loc]
    cuisine = rng.choice(cuis_names)
    rtype = rng.choice(type_names, p=TYPE_WEIGHTS)
    base, p_online, p_book = TYPES[rtype]

    cost = base * p_mult * CUISINES[cuisine] * rng.lognormal(0, 0.25)
    cost = int(np.clip(round(cost / 50) * 50, 100, 5000))

    rating = 3.5 + r_bias + min(cost, 3000) * 0.00012 + rng.normal(0, 0.35)
    rating = round(float(np.clip(rating, 2.0, 4.9)), 1)

    votes = int(rng.lognormal(5.0 + (rating - 3.5) * 0.8, 0.9))
    name = f"{rng.choice(PREFIX)} {rng.choice(SUFFIX)}"

    rows.append({
        "restaurant_id": 1000 + i,
        "restaurant_name": name,
        "locality": loc,
        "zone": zone,
        "cuisine": cuisine,
        "restaurant_type": rtype,
        "avg_cost_for_two": cost,
        "rating": rating,
        "votes": votes,
        "online_delivery": "Yes" if rng.random() < p_online else "No",
        "table_booking": "Yes" if rng.random() < p_book else "No",
        "opened_year": int(rng.integers(2005, 2026)),
    })

df = pd.DataFrame(rows)

# --- add realistic mess so the cleaning step has something to do ---
miss = rng.choice(df.index, size=int(0.03 * N), replace=False)
df.loc[miss, "rating"] = np.nan                                  # missing ratings
dups = df.sample(25, random_state=1)
df = pd.concat([df, dups], ignore_index=True)                     # duplicate rows
messy = rng.choice(df.index, size=60, replace=False)
df.loc[messy, "locality"] = df.loc[messy, "locality"].str.upper() + " "  # inconsistent text

df.to_csv("data/restaurants_raw.csv", index=False)
print(f"Saved data/restaurants_raw.csv  ->  {len(df)} rows")
