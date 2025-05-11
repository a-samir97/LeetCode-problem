def find_knapsack(capacity, weights, values, n):
    memo = {}

    def helper(capacity, weights, values, n):
        if n <= 0 or capacity <= 0:
            return 0
        
        if (capacity, n) in memo:
            return memo[(capacity, n)]
            
        inn = 0
    
        # included
        if weights[n-1] <= capacity:
            inn = helper(capacity-weights[n-1], weights, values, n-1) + values[n-1]
    
        # not included
        notinn = helper(capacity, weights, values, n-1)
        
        memo[(capacity, n)] = max(notinn, inn)
        return memo[(capacity, n)]
    return helper(capacity, weights, values, n)