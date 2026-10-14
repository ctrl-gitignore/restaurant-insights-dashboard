# Dashboard Build Guide (Power BI Desktop)

Theme suggestion: dark charcoal background (#1F2937), accent orange (#F97316), secondary teal (#14B8A6).
Set via **View > Themes** or just format each visual.

## Page 1 - Overview
| Visual | Fields |
|---|---|
| 5 x Card | Total Restaurants, Avg Rating, Avg Cost for Two, Online Delivery %, Table Booking % |
| Clustered column | X: `rating_band`  Y: Total Restaurants |
| Donut | Legend: `restaurant_type`  Values: Total Restaurants |
| Bar (Top 10) | Y: `cuisine`  X: Total Restaurants (Top N filter = 10) |
| Slicers | `zone`, `cuisine`, `restaurant_type` |

## Page 2 - Pricing Analysis
| Visual | Fields |
|---|---|
| Scatter | X: `avg_cost_for_two`  Y: `rating`  Details: `restaurant_id`  Size: `votes`  Legend: `price_band` |
| Clustered column | X: `price_band`  Y: Avg Rating |
| Bar | Y: `cuisine`  X: Avg Cost for Two (sorted desc) |
| Bar | Y: `cuisine`  X: Value Score (sorted desc) |
| Slicers | `zone`, `restaurant_type` |

## Page 3 - Locality Analysis
| Visual | Fields |
|---|---|
| Bar | Y: `locality`  X: Avg Rating (sort desc) |
| Bar | Y: `locality`  X: Avg Cost for Two |
| Matrix | Rows: `zone` > `locality`  Values: Total Restaurants, Avg Rating, Avg Cost for Two, Value Score |
| Stacked column 100% | X: `zone`  Y: Total Restaurants  Legend: `price_band` |
| Slicers | `cuisine`, `price_band` |

Turn on **Conditional formatting > Background color** for Avg Rating in the matrix (red -> green).

## Insights to write on the dashboard (text box)
After building, look at your visuals and write 3-4 bullet insights, e.g. which zone has the highest
average cost, whether higher price actually means higher rating, which locality gives best value.
Write what YOUR charts show - do not copy generic text.
