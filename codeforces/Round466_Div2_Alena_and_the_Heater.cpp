#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, x;
    cin>>n;
    vector<int> a;
    for(int i = 0; i < n; i++)
    {
        cin>>x;
        a.push_back(x);
    }
    string b;
    cin>>b;

    int l = 0, r = 0;
	int k = 0;
	for(int i = 4; i < n; i++)
	{
		if(b[i] != b[i-1])		//then we are talking
		{
			if(b[i] == 0)//then we are talking about r
                r = min(r, min_element(a.begin()+k,a.begin()+k+4)-1);
			else
                l = max(l, max_element(a.begin()+k, a.begin()+k+4)+1);
		}
	}
	cout<<l<<" "<<r;
	return 0;
}
