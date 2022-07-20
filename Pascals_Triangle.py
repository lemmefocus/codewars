

def generate(numRows):
    if numRows == 1:
        return [[1]]
    else:
        initial_list = [[1], [1, 1]]
        for i in range(numRows - 2):

            temp = initial_list[-1].copy()
            num_iter = len(temp) - 2

            for j in range(num_iter):
                temp.pop(1)

            index_start, index_end = 0, 1
            next_list = initial_list[-1].copy()
            for n in range(len(next_list) - 1):
                my_sum = next_list[index_start] + next_list[index_end]
                temp.insert(1, my_sum)
                index_start = index_start + 1
                index_end = index_end + 1

            initial_list.append(temp)

        return initial_list


print(generate(5))
