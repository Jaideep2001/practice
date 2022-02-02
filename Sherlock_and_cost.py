def cost(B):
    a=0
    b=0
    for i in range(1,len(B)):
        new_a=max((abs(B[i]-B[i-1])+a),(abs(B[i]-1)+b))
        new_b=max((abs(1-B[i-1])+a),b)
        a=new_a;b=new_b
    return max(a,b)
