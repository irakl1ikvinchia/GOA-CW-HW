# import random

# def r_p_s_cheat(opponent_move):
#     wins_against = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
#     loses_against = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    
#     if random.random() < 0.9:
#         return wins_against[opponent_move]
#     else:
#         return loses_against[opponent_move]



# def two_oldest_ages(ages):
#     agess = sorted(ages)
#     return agess[-2:]


# def halving_sum(n): 
#     total = 0
#     while n > 0:
#         total += n
#         n //= 2
#     return total