# https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?python=1

# Workers With The Highest Salaries
# Find the titles of workers that earn the highest salary. Output 
# the highest-paid title or multiple titles that share the highest salary.

# Import your libraries
import pandas as pd
import numpy as np

# merge both dfs to get the worker title + preserve only worker_title and salary columns
worker_title = (
    worker
    .merge(title, left_on='worker_id', right_on='worker_ref_id', how='left')[['worker_title', 'salary']]
    .assign(ranking=lambda r: r.salary.rank(method='dense', ascending=False))
    .sort_values(by=['ranking'], ascending=True)
    )

## ways to filter a dataframe
# 1. loc
worker_title.loc[(worker_title.ranking == 1)]
# 2. query (which can be used conveniently inside the chained assignments)
worker_title.query('ranking == 1')
# 3. iloc + np.where()
worker_title.iloc[np.where(worker_title['ranking'] == 1)]



# OUTPUT:
# worker_title | salary | ranking 
