#include<iostream>
using namespace std;

int main(){
int tes,t,n,i,j,k,z,l,cou=0;
cin>>tes;
for(t=0;t<tes;t++)
{cin>>n;
cou=0;
z=1;
int a[n][n],b[n][n];
for(i=0;i<n;i++)
{for(j=0;j<n;j++)
    {   cin>>k;
        a[i][j]=k;
        b[i][j]=z;
        z=z+1;
    }
}

for(int l=n-1;l>0;l--)
{int fl=0;
//row wise comparison
for(i=0;i<l;i++){
    if(a[l][i]!=b[l][i])
    {  cou=cou+1;
        fl=1;
        break;
    }
}
//column wise comparison
if(fl==0)
{for(i=0;i<l;i++){
    if(a[i][l]!=b[i][l])
    {   cou=cou+1;
        fl=1;
        break;
    }
}
}
//do transformation
if(fl==1)
{fl=0;
    int c[l+1][l+1];
for(i=0;i<=l;i++)
{   for(j=0;j<=l;j++)
{    c[i][j]=a[j][i];}}
//replacing
for(i=0;i<=l;i++)
{   for(j=0;j<=l;j++)
{a[i][j]=c[i][j];}}

}
    
}

cout<<cou<<endl;
}
    return 0;
}