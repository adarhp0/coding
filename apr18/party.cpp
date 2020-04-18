#include <iostream>
#include <queue>
#include <vector>
using namespace std;
void prlvl(vector<int> graph[], int n)
{
    int i, x, m;
    queue<int> qu;
    int level[n + 1], visi[n + 1];
    for (i = 0; i <= n; i++)
        visi[i] = 0;
    qu.push(0);
    level[0] = 0;
    while (!qu.empty())
    {
        x = qu.front();
        //cout << "hell" << x << endl;
        qu.pop();
        for (i = 0; i < graph[x].size(); i++)
        {
            int b = graph[x][i];
            if (!visi[b])
            {
                visi[b] = 1;
                qu.push(b);
                level[b] = level[x] + 1;
            }
        }
    }
    m = -1;
    for (i = 1; i <= n; i++)
    {
        //cout << "level" << level[i] << endl;
        if (m < level[i])
            m = level[i];
    }
    cout << m << endl;
}
int main()
{
    int n, a, i;

    cin >> n;
    vector<int> graph[n + 1];
    for (i = 1; i <= n; i++)
    {
        cin >> a;
        if (a == -1)
        {
            graph[0].push_back(i);
        }
        else
        {
            graph[a].push_back(i);
        }
    }
    prlvl(graph, n);

    return 0;
}