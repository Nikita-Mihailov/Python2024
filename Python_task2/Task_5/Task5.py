set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}
combined_set = set1.union(set2)
final_set = combined_set.union(set3)
not_in_sets = list(set(range(1, 80)) - final_set)
difference = final_set.difference(not_in_sets)
print("Список элементов, которые не вошли в множества:", not_in_sets)
print("Разница всех элементов множества и списка:", difference)