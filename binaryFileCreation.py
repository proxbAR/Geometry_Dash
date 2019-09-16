import pickle

high_scores = {}

with open('highScores.dat','ab') as f:
    pickle.dump(high_scores,f)
    
