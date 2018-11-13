#对字典进行排序，求最大最小值
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
#zip() 函数创建的是一个只能访问一次的迭代器
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

price_sorted = sorted(zip(prices.values(),prices.keys()))
print(price_sorted)