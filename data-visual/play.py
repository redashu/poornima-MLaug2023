import matplotlib.pyplot as plt 
players=['virat','dhoni','pathan','sachin']
runs=[200,234,120,300]

# condition list 
pl1=[]
run1=[]
for i in range(len(players)):
    if runs[i] > 200:
        pl1.append(players[i])
        run1.append(runs[i])
# now creating graphs 