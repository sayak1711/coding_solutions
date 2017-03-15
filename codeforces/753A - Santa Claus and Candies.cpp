#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, total = 0, i;
    cin>>n;
    
    int v[n] = {0};
    v[0] = 1;
    total = v[0];
    
    for(i = 1; i < n; i++)
    {
        if((total + v[i-1] + 1) > n)
            break;
        v[i] = v[i-1] + 1;
        total += v[i];
    }
    
    i--;
    int k = i;
    if(total < n)
    {
        for(i; i >= 0; i--)
        {
            if(total == n)
                break;
            v[i] += 1;
            total += 1;
        }
    }
    
    cout<<(k+1)<<endl;
    for(int j = 0; j <= k; j++)
    {
        cout<<v[j]<<" ";
    }
    
    return 0;
}