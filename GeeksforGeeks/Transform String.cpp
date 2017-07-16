#include<iostream>
#include<string>
#include<bits/stdc++.h>
using namespace std;

bool isPossible(string a, string b)
{
    int l1 = a.length(), l2 = b.length();
    if(l1 != l2)    return false;
    unordered_map<char,int> mymap;
    for(int i = 0; i < l1; i++)
        mymap[a[i]]++;
    for(int i = 0; i < l2; i++)
    {
        if(mymap.find(b[i]) != mymap.end())
        {
            mymap[b[i]]--;
            if(mymap[b[i]] == 0)
                mymap.erase(b[i]);
        }
        else    return false;
    }
    return true;
}

int minsteps(string a, string b)
{
    if(!isPossible(a,b))    return -1;
    int steps = 0;
    int l1 = a.length();
    int l2 = b.length();
    int res = 0;

    int i = l1-1, j = l2-1;
    while(i >= 0 && j >= 0)
    {
        if(a[i] == b[j])
        {
            i--;
            j--;
        }
        else
        {
            i--;
            res++;
        }
    }
    
    return res;
}

int main() 
{
	int t;
	string a, b;
	cin>>t;
	while(t--)
	{
	    cin>>a>>b;
	    cout<<minsteps(a,b)<<endl;
	}
	return 0;
}