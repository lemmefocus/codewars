def mix(string1, string2):
    dict_count_string1, dict_count_string2 = dict(), dict()
    new_string, result_string = '', ''
    string1_list, string2_list, unique_result_list, result_list_sorted = [], [], [], []
    if len(string1) > 0 and len(string2) > 0:
        for word1 in string1.strip():
            if word1.islower():
                string1_list.append(word1)

        for word2 in string2.strip():
            if word2.islower():
                string2_list.append(word2)

    for i in "".join(string1_list):
        dict_count_string1[i] = "".join(string1_list).count(i)

    for j in "".join(string2_list):
        dict_count_string2[j] = "".join(string2_list).count(j)

    for key1, value1 in dict_count_string1.items():
        for key2, value2 in dict_count_string2.items():
            if key1 == key2 and value1 > value2:
                new_string = new_string + "1" + ":" + str(key1 * value1) + "/"
            if key1 == key2 and value1 < value2:
                new_string = new_string + "2" + ":" + str(key2 * value2) + "/"
            if key1 == key2 and value1 == value2 and value1 > 1:
                new_string = new_string + "=:" + str(key2 * value2) + "/"
            if key1 not in dict_count_string2 and value1 > 1:
                new_string = new_string + "1" + ":" + str(key1 * value1) + "/"
            if key2 not in dict_count_string1 and value2 > 1:
                new_string = new_string + "2" + ":" + str(key2 * value2) + "/"

    result_list = new_string[:len(new_string)-1].split("/")

    for j in result_list:
        if j not in unique_result_list:
            unique_result_list.append(j)
    try:
        result_list_sorted = sorted(unique_result_list, key=lambda x: (-len(x), not x[0].isdigit(), x[0], x[2]))
        return "/".join(result_list_sorted)
    except IndexError:
        return "/".join(result_list_sorted)