#include<iostream>
using namespace std;

int main()
{
    int tes,n,a[100],men_cou=0,i,j,t,op;
    cin>>tes;
    for(t=0;t<tes;t++)
    {
        cin>>n;
        men_cou=0;
        for(i=0;i<n;i++)
        {
         cin>>a[i];   
        }
        
        op=0;
        for(i=0;i<n;i++)
        {men_cou=0;
        if(a[i]==1)
            {
                
                for(j=i+1;j<n;j++)
            {men_cou++;
                if(a[j]==1 && men_cou<6)
                {op=1;
                    break;
                }
                else if(a[j]==1 && men_cou >=6)
                {op=2;
                    break;
                }
                else if(a[j]==0 && men_cou>=6)
                {
                    op=2;
                    break;
                }
            }}
            if(op==1)
            {break;
            }

        }
        if(op==1)
        cout<<"NO"<<endl;
        else
        {
            cout<<"YES"<<endl;
        }
        
    }

    return 0;
}