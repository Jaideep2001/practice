def ranker(ranked):
    rankings=[]
    for i in range(len(ranked)):
        if i==0:
            rankings.append(1)
        else:
            if ranked[i]==ranked[i-1]:
                rankings.append(rankings[-1])
            else:
                rankings.append(rankings[-1]+1)
    return rankings
    

def climbingLeaderboard(ranked, player):
    lis=[]
    for i in range(len(player)):
        ranked.append(player[i])
        ranked.sort(reverse=True)
        a=ranked.index(player[i])
        rankings=ranker(ranked)
        lis.append(rankings[a])
        ranked.pop(a)
    return lis
