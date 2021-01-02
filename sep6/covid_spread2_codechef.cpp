#include<iostream>
#include<vector>
using namespace std;

int main(){
int tes,t,n,i,j,s[5],bc,wc,ti,tmod,mtime[5][5];
cin>>tes;
for(t=0;t<tes;t++)
{cin>>n;
for(i=0;i<5;i++)
for(j=0;j<5;j++)
mtime[i][j]=-1;
for(i=0;i<n;i++)
{cin>>s[i];
}
vector<int> cl[n];
for(i=0;i<n;i++)
{for(j=0;j<n;j++)
{
    if(i!=j)
    //find meet time
    {if((j-i)%(s[i]-s[j])==0)
    tmod=(j-i)%(s[i]-s[j]);
    ti=(j-i)/(s[i]-s[j]);
    mtime[i][j]=ti;
    mtime[j][i]=ti;
    }
}

}
for(i=0;i<5;i++)
for(j=0;j<5;j++)
cout<<mtime[i][j]<<" ";
}
    return 0;
}