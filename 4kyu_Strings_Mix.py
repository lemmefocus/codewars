"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.
We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.
The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.
In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
"""

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