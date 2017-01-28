#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool bsearch(int s, vector<int> v)
{
    int first = 0, n = v.size();
	int last = n-1;
	int middle = (first+last)/2;
	while (first <= last)
	{
		if(v[middle] < s)
		{
			first = middle + 1;
		}
		else if(v[middle] == s)
		{
			return true;
		}
		else
		{
			 last = middle - 1;
		}
		middle = (first + last)/2;
	}
	
	return false;
}    

int main() 
{
    string st;
    cin>>st;
    int n = st.size();
    vector<int> v(n,0);
    int j = 0;
    
    if(n > 0)
        v[0] = ((int)st[0] - 96);
    
    for(int i = 1; i < st.size(); i++)
    {
        if(st[i] == st[i-1])
        {
            j++;
            v[j] = v[j-1] + ((int)st[i] - 96); 
        }
        
        else
        {
            j++;
            v[j] = ((int)st[i] - 96);
        }    
    }
    
    int q, inp;
    cin>>q;
    sort(v.begin(),v.end());
    
    while(q--)
    {
        cin>>inp;
        if (bsearch(inp,v))
            cout<<"Yes\n";
        else
            cout<<"No\n";
    }   
    
    return 0;
}
