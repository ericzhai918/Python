from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['not'])
print(word_counts['eyes'])

# 如果你想手动增加计数
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])

# 更快捷的方法
word_counts.update(morewords)
print(word_counts)

# 数学运算

a = Counter(word)
b = Counter(morewords)

print(a - b)
print(a + b)



#作为输入， Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象。
#在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上
#Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具