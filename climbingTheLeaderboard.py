def climbingLeaderboard(ranked, player):
    rankedT=list(dict.fromkeys(ranked))
    rankedT=tuple(rankedT[::-1])
    length=len(rankedT)
    res=[]
    i=0
    for play in player:
        while (i<length) and rankedT[i]<=play:
            i=i+1
        res.append(length-i+1)
    return res
