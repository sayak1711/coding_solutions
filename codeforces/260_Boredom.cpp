#include<iostream>
#include<algorithm>
using namespace std;

typedef long long ll;
#define MAX 100005

int main()
{
    ll freq[MAX] = {0};
    int n,x;
    cin>>n;
    int high = -1;
    
    //count frequency
    for(int i = 0; i < n; i++)
    {
        cin>>x;
        freq[x]++;
        if(x > high)
            high = x;  //the maximum index where our answer lies
    }
    
    //now we will avoid using another matrix and use our frequency matrix itself
    //as the dp matrix
    
    for(int i = 2; i <= high; i++)
    {
        freq[i] = max(freq[i-1],freq[i-2]+freq[i]*i);
    }
    
    /*
    for each element we have to option: select it or don't select it
    note that dp[i] (freq[i] in our case) stores the max points that can be obtained
    by considering elements upto i
    when we remove a particular no. we remove all other instances of it. so we do
    i*freq[i] and don't consider its previous element(i-1) as (i-1)th element is 
    ak-1. we pick solution upto i-2 instead. but if we pick (i-1) we don't pick i
    because as we know ak+1 is to be eliminated.
    */
    cout<<freq[high];
    return 0;
}