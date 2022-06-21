"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""


def anagrams(word, words):
    word_dict, dict1, result = {}, {}, []

    if len(word) > 0:
        word_set = set(word)
        for j in word_set:
            word_dict[j] = word.count(j)

        for i in words:
            my_set = set(i)

            for j in my_set:
                dict1[j] = i.count(j)

            if word_dict == dict1:
                result.append(i)
            else:
                dict1.clear()

        return result

    else:
        return []