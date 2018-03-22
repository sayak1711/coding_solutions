#include <algorithm>
#include <vector>
#include <iostream>
#include <bits/stdc++.h>
#include <iomanip>

using namespace std;

int main()
{
    int t, n, i;
    double a, incprice, sp, loss, dis;
    vector<double> price;
    vector<double> quantity;
    vector<double> discount;
    cin>>t;
    
    while(t--)
    {
        cin>>n;
        for(i = 0; i < n; i++)
        {
            cin>>a;
            price.push_back(a);
            cin>>a;
            quantity.push_back(a);
            cin>>a;
            discount.push_back(a);
            dis = discount[i]/100.0000;
            incprice = price[i]+(price[i]*dis);
            sp = incprice-(incprice*dis);
            if(sp < price[i])
            {
                //then we have a loss
                loss += quantity[i]*(price[i]-sp);
            }
        }
        cout<<fixed;
        cout<<setprecision(4);
        cout<<loss<<endl;
        loss = 0.0000;
        price.clear();
        quantity.clear();
        discount.clear();
    }
    return 0;
}