
from collections import defaultdict

def balletCount(ballots, discount=0.9):
    if not len(ballots):
        return []
    
    discounted_vote_count = defaultdict(int)
    recency = {}
    for i, ballot in enumerate(ballots):
        for pref, candidate in enumerate(ballot):
            discounted_vote_count[candidate] += discount**pref
            recency[candidate] = i

    candidate_order = []
    for candidate in discounted_vote_count.keys(): 
        candidate_order.append((discounted_vote_count[candidate], recency[candidate], candidate))
    candidate_order = sorted(candidate_order, reverse=True)
    return [can for (votes, rec, can) in candidate_order]
    


ballots = [ 
    ['A','B', 'C', 'D'],
    ['E','B', 'A', 'D'],
    ['A','F', 'C', 'D'],
    ['C','B', 'K', 'D']
]
print(balletCount(ballots))



# test case 1 
ballots = [ 
    ['A','B'],
    ['A','B'],
    ['A','B'],
    ['F','C']
]
print(balletCount(ballots))


# test case 2
ballots = [ 
    ['A','C'],
    ['B','A'],
    ['A','B'],
    ['B','C']
]
print(balletCount(ballots))


# # test case 1 
ballots = [ 
    ['A','B'],
    ['A','B'],
    ['A','B'],
    ['F','B']
]
print(balletCount(ballots))

