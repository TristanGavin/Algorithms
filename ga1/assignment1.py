'''
    This file contains the template for Assignment1.  You should fill the
    function <majority_party_size>.  The function, recieves two inputs:
      (1) n: the number of delegates in the room, and
      (2) same_party(int, int): a function that can be used to check if two members are
      in the same party.

    Your algorithm in the end should return the size of the largest party, assuming
    it is larger than n/2.

    I will use <python3> to run this code.
'''


def majority_party_size(n, same_party):
    '''
        n (int): number of people in the room.
        same_party (func(int, int)): This function determines if two delegates
            belong to the same party.  same_party(i,j) is True if i, j belong to
            the same party (in particular, if i = j), False, otherwise.

        return: The number of delegates in the majority party.  You can assume
            more than half of the delegates belong to the same party.
    '''
# Replace the following line with your code.
    # Tristan's Algorithm
    # O(n) time 
    # looked at a description on wikipedia https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm 
    # no code was coppied.
    people = list(range(n))
    index = 0
    count = 1
    for person in people[1:]:
        if same_party(person, index):
            count += 1 
        else:
            count -= 1
        if count == 0:
            index = person
            count = 1
    
    maj_size = 0
    for i in people:
        if same_party(i, index):
            maj_size += 1
    return maj_size



# Sam's algorithm
# time complexity nlog(n) time.
# def majority_party_size(n, same_party):
#     elems = list(range(n))
#     elem = majority_element(elems, same_party)
#     return element_count(elem, elems, same_party)

# def element_count(a, xs, equals):
#     count = 0
#     for x in xs:
#         if equals(a, x):
#             count += 1
#     return count

# def majority_element(xs, equals):
#     if len(xs) == 1:
#         return xs[0]
#     else:
#         m = len(xs) // 2
#         left = majority_element(xs[:m], equals)
#         lcount = element_count(left, xs, equals)
#         right = majority_element(xs[m:], equals)
#         rcount = element_count(right, xs, equals)
#         if equals(left, right):
#             return left
#         elif lcount > rcount:
#             return left
#         elif rcount > lcount:
#             return right
#         else:
#             return -1



# First attempt algorithm 
# O(n^2)
    # people = list(range(n))
    # counts = {}
    # for person in people:
    #     for party, count in counts.items():
    #         if same_party(person, party):
    #             counts[party] += 1
    #             break
    #     else:
    #         counts[person] = 1
    # majority = max(counts.values())
    # return majority