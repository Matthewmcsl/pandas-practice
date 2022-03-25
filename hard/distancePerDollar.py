# https://platform.stratascratch.com/coding/10302-distance-per-dollar?python=1

# Distance Per Dollar

# You’re given a dataset of uber rides with the traveling distance (‘distance_to_travel’)
# and cost (‘monetary_cost’) for each ride. For each date, find the difference between the
# distance-per-dollar for that date and the average distance-per-dollar for that year-month.
# Distance-per-dollar is defined as the distance traveled divided by the cost of the ride.

# The output should include the year-month (YYYY-MM) and the absolute average difference in
# distance-per-dollar (Absolute value to be rounded to the 2nd decimal).

# You should also count both success and failed request_status as the distance and cost
# values are populated for all ride requests. Also, assume that all dates are unique in
# the dataset. Order your results by earliest request date first.


# Import your libraries
import pandas as pd


# table 1 =
original_table = uber_request_logs[
    ["request_date", "distance_to_travel", "monetary_cost"]
]

original_table["request_date"] = original_table.request_date.apply(
    lambda t: t.strftime("%Y-%m")
)

# get the monthly average
avg_dpd_by_month = (
    original_table.groupby(["request_date"])["distance_to_travel", "monetary_cost"]
    .sum()
    .reset_index()
    .assign(
        monthly_avg_distance_per_dollar=lambda x: x.distance_to_travel / x.monetary_cost
    )
)[["request_date", "monthly_avg_distance_per_dollar"]]

original_table = (
    original_table.assign(
        date_avg_dist_per_dol=lambda x: x.distance_to_travel / x.monetary_cost
    )
)[["request_date", "date_avg_dist_per_dol"]]

# now we merge back the monthly average
res = original_table.merge(avg_dpd_by_month, on="request_date", how="left").assign(
    occurrence_count=lambda x: x.groupby(
        "request_date"
    ).monthly_avg_distance_per_dollar.transform("count"),
    abs_diff=lambda y: abs(y.date_avg_dist_per_dol - y.monthly_avg_distance_per_dollar),
)

occur = res.drop_duplicates(subset=["request_date"])[
    ["request_date", "occurrence_count"]
]

ans = res.groupby("request_date")["abs_diff"].sum().reset_index()

ans = (
    ans.merge(occur, on="request_date", how="left")
    .assign(mean_deviation=lambda x: x.abs_diff / x.occurrence_count)
    .round(2)
)

ans[["request_date", "mean_deviation"]]

# OUTPUT:
# Request_date | mean_deviation
