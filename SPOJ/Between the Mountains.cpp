#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long
using namespace std;

int main() 
{
	int t;
	int n1, n2;
	vector<ll> m1;
	vector<ll> m2;
	
	cin>>t;
	while(t--)
	{
		cin>>n1;
		ll inp;
		for(ll i = 0; i < n1; i++)
		{
			cin>>inp;
			m1.push_back(inp);
		}

		cin>>n2;
		for(ll i = 0; i < n2; i++)
		{
			cin>>inp;
			m2.push_back(inp);
		}
		
		sort(m1.begin(),m1.end());
		sort(m2.begin(),m2.end());
		
		int p1 = 0, p2 = 0;                //two pointers
		ll min = 1000000;
		while(p1 < n1 && p2 < n2)
		{
			if(m1[p1] < m2[p2])
			{
				if((m2[p2] - m1[p1]) < min)
					min = m2[p2] - m1[p1];
				p1++;
			}
			
			else if(m1[p1] > m2[p2])
			{
				if((m1[p1] - m2[p2]) < min)
					min = m1[p1] - m2[p2];
				p2++;
			}
			
			else if(m1[p1] == m2[p2])
			{
				min = 0;
				cout<<0<<endl;
				goto here;
			}
		}
		cout<<min<<endl;
		here: m1.clear();
		m2.clear();
	}
	return 0;
}