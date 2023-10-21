def knapsack(values, weights, capacity):
    """
    Decide which items to pick to maximize the total value without exceeding the capacity.
    """
    num_items = len(values)
    
    # Create a table to store results of subproblems
    dp = []
    for i in range(num_items + 1):
        dp.append([0] * (capacity + 1))

    # Fill the dp table
    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            
            # If the weight of the item is less than or equal to w
            if weights[i-1] <= w:
                # Check if the value of the current item + value of the item that we could afford 
                # with the remaining weight is greater than the value without the current item
                if values[i-1] + dp[i-1][w-weights[i-1]] > dp[i-1][w]:
                    dp[i][w] = values[i-1] + dp[i-1][w-weights[i-1]]
                else:
                    dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = dp[i-1][w]

    return dp[num_items][capacity]
