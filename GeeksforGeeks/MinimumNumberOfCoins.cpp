//https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/
#include <iostream>
using namespace std;

int number_of_coins(int denominations[], int value)
{
    int l = 0, r = 8;
	int highest = -1;
	while(l <= r)
	{
	    int mid = l+(r-l)/2;
	    if(denominations[mid] < value)
	    {
	        highest = max(highest, denominations[mid]);
	        l = mid+1;
	    }
	    else if(value < denominations[mid])
	    {
	        r = mid-1;
	    }
	    else if(value == denominations[mid])
	        return value;
	}
	return highest;
}

int main() 
{
	int denominations[] = { 1, 2, 5, 10, 20, 50, 100, 500, 1000};
	int value = 0;
	cin>>value;
	//find largest number smaller than or equal to this
	//for that best will be to use binary search
	//even if there aren't too many denominations here it is better use a generic approach
	int count = 0;
	while(value >= 1)
	{
	    int highest = number_of_coins(denominations, value);
	    count += value/highest;
	    value = value%highest;
	}
	cout<<count;
	return 0;
}