# indexing -> accessing elements of a sequence using []
# [] -> indexing operator
# [start: end: step]
# start is inclusive, end is exclusive

credit = "1234-5678-9012-3456"

credit[0]  # first character of the string array
credit[-1]  # first char from the end
credit[:4]  # all char from 0 till 3
credit[5:9]  # all char from 5 till 8
credit[5:]  # all char from 5 till the end
credit[::2]  # all char at intervals of 2 (13-6891-46)
credit[::-1]  # reverses the string

# the -1 reversing works as the array starts at 0. with a step of -1, it
# goes backwards, ending up at the last digit and going back from there
# and thus printing the string in reverse
