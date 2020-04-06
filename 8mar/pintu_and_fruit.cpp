#include <iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> a;
    int t,tes,n,m,i,j,f[51],p[51],fr[51],g1,g2,min,su=0;
    cin>>tes;
    for(t=0;t<tes;t++){
        su=0;
        cin>>n;
        cin>>m;
        cout<<"m"<<m<<endl;
        f[0]=0;
        p[0]=0;
        for(i=0;i<=m;i++)
        fr[i]=0;
        for(i=1;i<=n;i++)
        cin>>f[i];
        for(i=1;i<=n;i++)
        cin>>p[i];
        for(i=1;i<=n;i++)
        {
            g1=f[i];
            g2=p[i];
            fr[g1]+=g2;
        }
        min=5000;
        cout<<"m1"<<m<<endl;
        for(i=1;i<=m;i++)
        {
            if(fr[i]<min && fr[i]!=0)
            min=fr[i];
        }
        for(i=1;i<=m;i++)
        {
            if(fr[i]==min)
            su+=fr[i];
            cout<<i<<" ";
        }
    cout<<su<<endl;
    }
    return 0;
}