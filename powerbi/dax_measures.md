# DAX Measures

Create these in Power BI Desktop: **Home > New measure** (select the `restaurants_clean` table first).
Copy-paste one at a time.

```DAX
Total Restaurants = DISTINCTCOUNT(restaurants_clean[restaurant_id])

Avg Rating = ROUND(AVERAGE(restaurants_clean[rating]), 2)

Avg Cost for Two = ROUND(AVERAGE(restaurants_clean[avg_cost_for_two]), 0)

Total Votes = SUM(restaurants_clean[votes])

Excellent Rated % =
DIVIDE(
    CALCULATE([Total Restaurants], restaurants_clean[rating] >= 4.1),
    [Total Restaurants]
)

Online Delivery % =
DIVIDE(
    CALCULATE([Total Restaurants], restaurants_clean[online_delivery] = "Yes"),
    [Total Restaurants]
)

Table Booking % =
DIVIDE(
    CALCULATE([Total Restaurants], restaurants_clean[table_booking] = "Yes"),
    [Total Restaurants]
)

Value Score = ROUND(DIVIDE([Avg Rating], [Avg Cost for Two]) * 1000, 2)

Premium Share % =
DIVIDE(
    CALCULATE([Total Restaurants], restaurants_clean[avg_cost_for_two] > 1000),
    [Total Restaurants]
)

Locality Rank (by Avg Rating) =
RANKX(ALL(restaurants_clean[locality]), [Avg Rating], , DESC, Dense)

Rating vs Overall Avg =
[Avg Rating] - CALCULATE([Avg Rating], ALL(restaurants_clean))
```

## What each one answers
| Measure | Business question |
|---|---|
| Total Restaurants | How big is the market we are looking at? |
| Avg Rating / Excellent Rated % | How good is the quality overall? |
| Avg Cost for Two / Premium Share % | How expensive is it? |
| Value Score | Which areas/cuisines give the best rating per rupee? |
| Online Delivery % / Table Booking % | How digital is the segment? |
| Locality Rank | Which localities lead on rating? |
