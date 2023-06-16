#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int n;
    std::cin >> n;

    std::vector<int> v;
    for (int i = 0; i < n; i++)
    {
        int num;
        std::cin >> num;
        v.push_back(num);
    }
    
    std::vector<int> dp(n, 1);
    int res = dp[0];
    for (int i = 1; i < n; i++)
    {
        if (v[i-1] < v[i])
        {
            dp[i] = std::max(dp[i], dp[i-1] + 1);
            res = std::max(res, dp[i]);
        }
    }
    
    std::cout << res << std::endl;
    return 0;
}