# T.C = O(n^2)
def brute(prices):
	n = len(nums)
	max_profit = 0
	for i in range(n):
		buy = prices[i]
		for j in range(i,n):
			sell = prices[j]
			max_profit = max(max_profit,sell-price)
	return max_profit

# T.C = O(n)
def optimal(prices):
	n = len(prices)
	mini_price = prices[0]
	max_profit = 0
	for i in range(1,n):
		profit = prices[i] - mini_price
		max_profit = max(max_profit,profit)
		mini_price = min(mini_price,prices[i])
	return max_profit

# T.C = O(n)
def optimal2(prices):
	n = len(prices)
	mini_price = float("inf")
	max_profit = 0
	for price in prices:
		if price < mini_price:
			mini_price = price
		elif price - mini_price > max_profit:
			max_profit = price - mini_price
