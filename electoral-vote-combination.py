dp = {}
def count_winning_combinations(i, curr_votes):
    if i == len(states):
        return 1 if curr_votes > target_votes else 0
    if (i, curr_votes) in dp:
        return dp[(i, curr_votes)]

    dp[(i, curr_votes)] = count_winning_combinations(i + 1, curr_votes + states[i]) + count_winning_combinations(i + 1, curr_votes)
    return dp[(i, curr_votes)]


states = [3, 4, 8]
total_votes = sum(states)
target_votes = total_votes // 2 + 1
print(total_votes, target_votes)

assert = count_winning_combinations(0, 0) == 3



votes_to_states = {
    3: ["Alaska", "Delaware", "Wyoming"],
    4: ["Hawaii"],
    5: ["Nebraska"],
    6: ["Arkansas"],
    7: ["Connecticut"],
    8: ["Kentucky"],
    9: ["Alabama"],
    10: ["Maryland"],
    11: ["Arizona"],
    12: ["Washington"],
    13: ["Virginia"],
    14: ["New Jersey"],
    15: ["North Carolina"],
    16: ["Georgia"],
    18: ["Ohio"],
    20: ["Illinois"],
    29: ["Florida"],
    55: ["California"]
}

states = []
for votes, state_list in votes_to_states.items():
    states.extend([votes] * len(state_list))
print(states)

total_votes = sum(states)
target_votes = total_votes // 2 + 1
print(total_votes, target_votes)

print(count_winning_combinations(0, 0))



