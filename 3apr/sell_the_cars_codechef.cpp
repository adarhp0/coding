#include<iostream>
#include<list>
#include<unordered_map>
#include<iterator>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int pr;
    int tes,t,n,i,j,k,ind,days,z,d1,d2;
    cin>>tes;
    list<int>:: iterator it;
    list<int>crp;
    unordered_map<int,int> umap;
    for(t=0;t<tes;t++)
    {
        pr=0;
        
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>k;
            if(k!=0)
            crp.push_back(k);
        }
        for(it=crp.begin();it!=crp.end();it++)
        {
            umap[*it]+=1;
        }

for (auto x : umap) 
{
    pr=pr+x.first*x.second;
}
d1=crp.size();
d2=((d1-1)*(d1))/2;
pr=pr-d2;

        crp.clear();
    
       // for(it=crp.begin();it!=crp.end();it++)
       // {cout<<*it;
       // }
        pr=pr%1000000007;
        cout<<pr;
    }
    return 0;
}