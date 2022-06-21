"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    pairs = [s[2*i:2*i+2] for i in range(len(s) // 2)]
    if len(s) % 2 == 1:
        pairs.append(f'{s[-1]}_')
    return pairs