import numpy as np
import pandas as pd
import random

# Parameters
num_anglers = 100
fishing_duration_mean = 4  # hours
catch_rate_mean = 2 # fish per hour

# Simulate angler data
angler_data = []
for i in range(num_anglers):
    fishing_duration = np.random.normal(fishing_duration_mean, 1)
    num_fish_caught = np.random.poisson(catch_rate_mean*fishing_duration)
    angler_data.append({
        'angler_id': i,
        'fishing_duration': fishing_duration,
        'num_fish_caught': num_fish_caught
    })

# Convert to pandas DataFrame for analysis
df = pd.DataFrame(angler_data)
print(df)
