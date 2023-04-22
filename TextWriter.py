#Writes current Any% stats to a file

def write(TotalRuns, TotalRNG, BushGoal):
    with open('TextOverlay.txt', 'w') as file:
        file.write('Total Runs: '+str(TotalRuns)+'\n')
        file.write('Total Runs with RNG: '+str(TotalRNG)+'\n')
        file.write('Bush Cutting Goal: '+str(BushGoal))
        file.close
        pass