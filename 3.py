# Write your solution for algorithm 2 below
def num_sorted(num_list):
    num_list_sorted = sorted(num_list, reverse = True)
    return num_list_sorted


num_lst = [1, 56, 18, 101, 4, 8, 20]
print(num_sorted(num_lst))