#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

string mat[200];
bool mark[200][200];
int dist[200][200];

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

int main()
{
    int t,n,m;
    cin>>t;
    while(t--)
    {
        cin>>n>>m;
        memset(mark,0,sizeof(mark));
        memset(dist,0,sizeof(dist));
        queue< pair<int,int> > q;
        pair<int,int> p;

        for(int i = 0; i < n; i++)
            cin>>mat[i];
        
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++)
            {
                if(mat[i][j] == '1')
                {
                    p.first = i;
                    p.second = j;
                    q.push(p);
                    mark[i][j] = 1;
                    dist[i][j] = 0;
                }
            }
        }
        //BFS
        pair<int,int> temp;
        while(!q.empty())
        {
            p = q.front();
            q.pop();
            for(int i = 0; i < 4; i++)
            {
                temp.first = p.first + dx[i];
                temp.second = p.second + dy[i];
                if(temp.first >= 0 && temp.first < n && temp.second >= 0 && temp.second < m )
                {
                    if(!mark[temp.first][temp.second])
                    {
                        q.push(temp);
                        mark[temp.first][temp.second] = 1;
                        dist[temp.first][temp.second] = dist[p.first][p.second] + 1;
                    }
                }
            }
        }

        for(int i = 0; i < n; i++)
        {
        	for(int j = 0; j < m; j++)
        		cout<<dist[i][j]<<" ";
        	cout<<endl;
        }
    }
    return 0;
}