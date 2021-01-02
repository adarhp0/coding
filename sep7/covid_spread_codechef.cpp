#include<iostream>
#include<vector>
#include<math.h>
#include<set>
using namespace std;

int main(){
int tes,t,n,i,j,k,s[5],ti,inf,t_thres;
float jgot;
cin>>tes;
for(t=0;t<tes;t++)
{    cin>>n;
int mtime[n][n];
for(i=0;i<n;i++)
for(j=0;j<n;j++)
mtime[i][j]=-1;
for(i=0;i<n;i++)
cin>>s[i];

vector<int> cl[n];
vector<int> visi[n];
for(i=0;i<n;i++)
for(j=0;j<n;j++)
{
    visi[i].push_back(0);
}
for(i=0;i<n;i++)
visi[i][i]=1;
for(i=0;i<n;i++)
{for(j=i+1;j<n;j++)
{if(s[i]-s[j]!=0)
    //find meet time
    {jgot=(j-i)/(s[i]-s[j]);
    if(floor(jgot)==ceil(jgot))
        {
            ti=floor(jgot);
            if(ti>0)
            {mtime[i][j]=ti;
    mtime[j][i]=ti;
    visi[i][j]=1;
    visi[j][i]=1;
    cl[i].push_back(j);
    cl[j].push_back(i);
            }
        }
    }
}}
//2nd part
for(i=0;i<n;i++)
{for(j=0;j<cl[i].size();j++)
{
    inf=cl[i][j];
    t_thres=mtime[i][inf];
    if(t_thres>0)
    {
        for(k=0;k<n;k++)
        {
            if(k!=i && t_thres<=mtime[inf][k])
            {if(visi[i][k]!=1)
                {cl[i].push_back(k);
                visi[i][k]=1;
                }
            if(mtime[i][k]>mtime[inf][k])
            mtime[i][k]=mtime[inf][k];
            } 
        }
    }
}
}
for(i=0;i<n;i++)
{
    cl[i].push_back(i);
}
vector<int>zxc;
for(i=0;i<n;i++)
{
set<int> af;
    for(j=0;j<cl[i].size();j++)
    {
af.insert(cl[i][j]);
    }
zxc.push_back(af.size());
af.clear();
}
int m1=10,m2=-1;
for(i=1;i<zxc.size();i++)
{
    if(m1>zxc[i])
    {
        m1=zxc[i];
    }
    else if(m2<zxc[i])
    {
        m2=zxc[i];
    }
}
cout<<m1<<" "<<m2<<endl;
}
    return 0;
}