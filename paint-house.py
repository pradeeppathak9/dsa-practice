# In this problem, we have `m` cakes placed in a row on a baking sheet - eg. Cake 1, Cake 2, Cake 3, ....

# - We'd like to decorate each cake either red, green, or blue.
# - For each combination of cake and color, we are given the amount of money it costs to decorate that cake with that color.
# - A cake cannot be decorated the same color as its neighbor cakes (left and right)
# - The goal is to decorate all of the cakes for the minimum total cost.

# /**
# *   Write a function
# * @arg costs[i][j] is the cost to decorate `ith` cake the `jth` color. j will be in the range [0,2] since we only consider RGB for this case.
# * @returns minimum total cost to decorate the cakes given the condition that a cake cannot be decorated the same color as its neighbor cakes (left and right)   e.g. costs =
 
#           R    G    B
# Cake 1    2    1    3
# Cake 2    3    2    1
# Cake 3    4    2    3
# Cake 4    5    2    1


# **/
# import math

# def decorate_cake(costs):   
#     def backtrack(i, prev_color, temp_cost):
#         ans = math.inf
#         for j in range(3):
#             if j == prev_color:
#                 continue
#             ans = min(ans, backtrack(i+1, j, temp_cost + costs[i][j]))
#         return ans
#     return backtrack(0, None, 0)


def decroate_cake_dp(costs):
  num_cakes, num_colors = len(costs), len(costs[0])
  prev_row_costs = costs[0]
  for i in range(1, num_cakes):
    curr_row_costs = costs[i][:]
    for j in range(num_colors):
      curr_row_costs[j] += min([ans[k] for k in range(num_colors) if k != j ] )
    prev_row_costs = curr_row_costs
  return min(prev_row_costs)






   


 
