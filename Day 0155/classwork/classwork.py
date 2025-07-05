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


# def valid_card(card):
#     card = card[::-1].replace(" ", "")
#     new_str = []
#     for i in range(len(card)):
#         if i % 2 != 0 and int(card[i]) * 2 > 9:
#             new_str.append(int(card[i]) * 2 - 9)
#         elif i % 2 != 0 and int(card[i]) * 2 < 10:
#             new_str.append(int(card[i]) * 2)
#         else:
#             new_str.append(int(card[i]))
#     return sum(new_str) % 10 == 0