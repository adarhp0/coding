#include <iostream>
#include <vector>
#include <queue>
#define loop(x, n) for (int x = 0; x < n; ++x)
using namespace std;
void bs(vector<int> g[], int n, int s)
{
    int i, a, b;
    int visi[n + 1] = {0};
    queue<int> qu;
    qu.push(s);
    while (!qu.empty())
    {
        a = qu.front();
        cout << a << "\t";
        qu.pop();
        loop(i, g[a].size())
        {
            b = g[a][i];
            if (!visi[b])
            {
                visi[b] = 1;
                qu.push(b);
            }
        }
    }
}

int main()
{
    int n, v, i, a, b, s;
    cout << "enter the number of vertices" << endl;
    cin >> n;
    vector<int> graph[n + 1];
    cout << "enter vertices" << endl;
    cin >> v;
    loop(i, v)
    {
        cin >> a >> b;
        graph[a].push_back(b);
    }
    cout << "start vertex" << endl;
    cin >> s;
    bs(graph, n, s);
    return 0;
}
