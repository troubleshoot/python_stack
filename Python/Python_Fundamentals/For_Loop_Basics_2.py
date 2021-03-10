# def biggie_size(list):
#   for i in range(len(list)):
#     if list[i] > 0:
#       list[i] = "big"
#   return list

# print(biggie_size([-1,3,5,-5]))

# def count_positives(list):
#   count = 0
#   for i in range(len(list)):
#     if list[i] > 0:
#       count = count + 1
#     if i == len(list) - 1:
#       list[i] = count
#   return list

# print(count_positives([-1,1,1,1]))

# def sum_total(list):
#   sum = 0
#   for i in range(len(list)):
#     sum = sum + list[i]
#   return sum

# print(sum_total([1,2,3,4]))

# def average(list):
#   sum = 0
#   for i in range(len(list)):
#     print(list[i])
#     sum = sum + list[i]
#   print(sum)
#   print(len(list))
#   return sum / len(list)

# print(average([1,2,3,4]))

# def length(list):
#   return len(list)

# print(length([37,2,1,-9]))

# def minimum(list):
#   min = list[0]
#   for i in range(len(list)):
#     if list[i] < min:
#       min = list[i]
#   return min

# print(minimum([37,2,1,-9]))

# def maximum(list):
#   max = list[0]
#   for i in range(len(list)):
#     if list[i] > max:
#       max = list[i]
#   return max

# print(maximum([37,2,1,-9]))

# def ultimate_analysis(list):
#   analysis = {}
#   analysis['sumTotal'] = 0
#   analysis['average'] = 0
#   analysis['minimum'] = list[0]
#   analysis['maximum'] = list[0]
#   analysis['length'] = len(list)
#   for i in range(len(list)):
#     analysis['sumTotal'] = analysis['sumTotal'] + list[i]
#     if list[i] > analysis['maximum']:
#       analysis['maximum'] = list[i]
#     if list[i] < analysis['minimum']:
#       analysis['minimum'] = list[i]
#   analysis['average'] = analysis['sumTotal'] / analysis['length']
#   return analysis

# print(ultimate_analysis([37,2,1,-9]))

# def reverse_list(list):
#   return [ele for ele in reversed(list)]

# print(reverse_list([37,2,1,-9]))