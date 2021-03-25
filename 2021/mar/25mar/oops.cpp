#include<iostream>
using namespace std;

class complex
{
    private: int a;
    public: int b;
    complex(int a1,int b1)
    {
        a=a1;
        b=b1;
    }
    public: void print()
    {
        cout<<"your output is"<<a<<"and"<<b<<endl;
    }
};
int main()
{
    complex c(10,15);
    c.print();
    
    return 0;
}