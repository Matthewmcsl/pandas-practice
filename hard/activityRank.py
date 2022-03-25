# https://platform.stratascratch.com/coding/10351-activity-rank?python=1

# Activity Rank

# Find the email activity rank for each user. Email activity rank is defined by the
# total number of emails sent. The user with the highest number of emails sent will
# have a rank of 1, and so on. Output the user, total emails, and their activity rank.
# Order records by the total emails in descending order. Sort users with the same
# number of emails in alphabetical order.

# In your rankings, return a unique value (i.e., a unique rank) even if multiple users
# have the same number of emails.

# Userid | total_emails | activity_rank (unique)

# Import your libraries
import pandas as pd

# Start writing code
user_with_count = (
    google_gmail_emails.groupby(["from_user"])["id"].count().to_frame().reset_index()
)

res = (
    user_with_count.assign(rank=lambda x: x.id.rank(method="first", ascending=False))
    .sort_values(by=["id", "from_user"], ascending=[False, True])
    .rename(columns={"id": "total_emails"})
)

# OUTPUT:
# from_user | total_emails | rank
