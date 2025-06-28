n=int(input("Enter number "))
if n==0:
    print(n)
if n==1:
    print(n)

dp=[0]*(n+1)
dp[0]=0
dp[1]=1
for i in range(2,len(dp)):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[-1])
