#include<iostream>
#include<set>
using namespace std;

int main(){
int t,i,n,k;
cin>>t;
set<int>s;
for(i=0;i<t;i++)
{
cin>>n;
s.clear();
if(n==0){
    cout<<1<<endl;
}
else{
for(int j=0;j<n;j++){
    cin>>k;
    if(k!=0)
    {s.insert(k);}

}
cout<<s.size()<<endl;
}
}
    return 0;
}