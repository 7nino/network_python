s1=[1,2,3,4,5]
s2=[2,3,5,6,7]
s3=[5,6,2,9,0]
def jiaoji(x,y,z):
    jihe=[]
    for i in x:
        if i in y:
            if i in z:
                jihe.append(i)
    return jihe 
print(jiaoji(s1,s2,s3))
