#include <iostream>
using namespace std;

int rev(int x)
{
	int num = 0, flag = 0;
	while(x)
	{
		if(x % 10 || flag)
		{
			num = (10*num) + (x%10);
			flag = 1;
		}
		x = x/10;
	}
	return num;
}

int main() 
{
	int t, n1, n2;
	cin>>t;
	
	while(t--)
	{
		cin>>n1>>n2;
		int revsum = rev(n1) + rev(n2);
		cout<<rev(revsum)<<endl;
	}
	
	return 0;
}