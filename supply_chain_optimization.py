--Python
# Initialize Class
model = LpProblem("Maximize Glass Co. Profits", LpMaximize)

# Define Decision Variables
wine = LpVariable('Wine', lowBound=0, upBound=None, cat='Integer')
beer = LpVariable('Beer', lowBound=0, upBound=None, cat='Integer')

# Define Objective Function
model += 5 * wine + 4.5 * beer

# Define Constraints
model += 6 * wine + 5 * beer <= 60
model += 10 * wine + 20 * beer <= 150
model += wine <= 6

# Solve Model
model.solve()
print("Produce {} batches of wine glasses".format(wine.varValue))
print("Produce {} batches of beer glasses".format(beer.varValue))


--<script.py> output:
    Produce 6.0 batches of wine glasses
    Produce 4.0 batches of beer glasses




    --Logistics planning problem
    -- The goal is to fulfill the regional demand at the lowest price.

from pulp import *

# Initialize Model
model = LpProblem("Minimize Transportation Costs", LpMinimize)

# Build the lists and the demand dictionary
warehouse = ['New York', 'Atlanta']
customers = ['East', 'South', 'Midwest', 'West']
regional_demand = [1800, 1200, 1100, 1000]
demand = dict(zip(customers, regional_demand))

# Define Objective
model += lpSum([costs[(w, c)] * var_dict[(w, c)] 
                for c in customers for w in warehouse])

# For each customer, sum warehouse shipments and set equal to customer demand
for c in customers:





Scheduling workers problem
# The class has been initialize, and x, days, objective function defined
model = LpProblem("Minimize Staffing", LpMinimize)
days = list(range(7))
x = LpVariable.dicts('staff_', days, lowBound=0, cat='Integer')
model += lpSum([x[i] for i in days])

# Define Constraints
model += x[0] + x[3] + x[4] + x[5] + x[6] >= 31
model += x[0] + x[1] + x[4] + x[5] + x[6] >= 45
model += x[0] + x[1] + x[2] + x[5] + x[6] >= 40
model += x[0] + x[1] + x[2] + x[3] + x[6] >= 40
model += x[0] + x[1] + x[2] + x[3] + x[4] >= 48
model += x[1] + x[2] + x[3] + x[4] + x[5] >= 30
model += x[2] + x[3] + x[4] + x[5] + x[6] >= 25

model.solve()