#include<iostream>
#include<vector>
#include <bits/stdc++.h>
using namespace std;

int main(){
int t,i,n,co=0;
cin>>t;
while(t--){

    cin>>n;
    vector<int> a(n);
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    sort(a.begin(),a.end());
    int cr=0;
    co=0;
    for(i=0;i<n;i++)
    {
        if(++cr==a[i])
        {
            cr=0;
            co++;
                    }
    }
    cout<<co<<endl;
}
    return(0);
}