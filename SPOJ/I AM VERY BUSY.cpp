#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

int main() 
{
	int t, N, m, n;
	cin>>t;
	while(t--)
	{
		cin>>N;
		vector<pair<int,int> > v;
		for(int i = 0; i < N; i++)
		{
			cin>>m;
			cin>>n;
			pair<int,int> p = make_pair(n,m); //putting end time first so that we
			v.push_back(p);                   //can sort on the basis of that 
		}
		
		sort(v.begin(),v.end());
		int last = 0;
		int count = 0;
		for(int i = 0; i < N; i++)
		{
			if(v[i].second >= last)
				{	
					count++;
					last = v[i].first;
				}
		}
		cout<<count<<endl;
	}
	return 0;
}