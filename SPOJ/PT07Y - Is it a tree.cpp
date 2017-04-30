#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool bfs(vector<int> edg[], int u, int n)
{
	queue<int> q;
	q.push(u);
	bool visited[n+1] = {false};
	int count = 0;
	while(!q.empty())
	{
		int p = q.front();
		visited[p] = true;
		q.pop();
		for(int i = 0; i < edg[p].size(); i++)
		{
			int k = edg[p][i];
			if(visited[k])	return false; //bcz there is cycle
			else	q.push(k);
		}
		count++;
	}
	if(count != n)	return false;
	else	return true;
}

int main() 
{
	int n,m;
	cin >>n>>m;
	vector<int> edg[n+1];
	while(m--)
	{
		int u,v;
		cin>>u>>v;
		edg[u].push_back(v);
	}
	//two things to be checked->isConnected and isAcyclic
	if(bfs(edg,1,n))
		cout<<"YES"<<endl;
	else
		cout<<"NO"<<endl;
	return 0;
}