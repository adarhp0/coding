#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void bf(vector<int> g[], int n, int s)
{
    int i, j, m;
    queue<int> q;
    int visi[n + 1] = {0};
    q.push(s);
    visi[s] = 1;
    while (!q.empty())
    {
        j = q.front();
        q.pop();
        cout << j << "\t";
        for (i = 0; i < g[j].size(); i++)
        {
            m = g[j][i];
            if (visi[m] == 0)
            {
                visi[m] = 1;
                q.push(m);
            }
        }
    }
}

int main()
{
    int n, e, i, j, a, b, s;
    cout << "enter number of vertices" << endl;
    cin >> n;
    vector<int> g[n + 1];
    cout << "enter number of edges" << endl;
    cin >> e;
    for (i = 0; i < e; i++)
    {
        cout << "enter edges" << endl;
        cin >> a >> b;
        g[a].push_back(b);
    }
    cout << "enter the start vertices" << endl;
    cin >> s;
    bf(g, n, s);
    return 0;
}