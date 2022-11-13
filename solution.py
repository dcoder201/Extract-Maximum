#User function Template for python3

class Solution:
    def extractMaximum(self,S): 
        # code here
        s=''
        res=[]
        for i in S:
            if ord(i)>=48 and ord(i)<=57:
                s+=i
            else:
                s=s+' ' 
        lis=s.split()
        if len(lis)==0:
            return -1
        else:
            fin=list(map(int,lis))
            k=max(fin)
            return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        print(ob.extractMaximum(S)) 

# } Driver Code Ends
