#include <iostream>
using namespace std;

int main() 
{
	while(true)
	{
		int a, b, c;
		cin>>a>>b>>c;
		if(a == 0 && b == 0 && c == 0)
			break;
		
		if((b-a) == (c-b))
		{
			cout<<"AP "<<(c + (c-b));
		}			

		else
		{
			//if any one is 0 it can't be GP because all have to be 0
			if(a != 0 && b != 0 && c != 0)
			{
				if((c/b) == (b/a))
				{
				   int ratio = (c/b);
				   cout<<"GP "<<(c * ratio);
				}
			}
		}
		cout<<endl;
	}
	return 0;
}