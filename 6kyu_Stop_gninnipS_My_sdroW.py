"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(sentence):
    if len(sentence) > 0:
        words = sentence.split()
        empty = ""
        for i in words:
            if len(i) >= 5:
                empty = empty + " " + i[::-1]
            else:
                empty = empty + " " + i
        return empty.lstrip()