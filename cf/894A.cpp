#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    string input;
    cin >> input;
    int len = input.length();

    vector<int> dp_Q = vector<int>(len, 0);
    vector<int> dp_QA = vector<int>(len, 0);
    vector<int> dp_QAQ = vector<int>(len, 0);

    dp_Q[0] = input[0] == 'Q' ? 1 : 0;
    dp_QA[0] = 0;
    dp_QAQ[0] = 0;

    for (int i = 1; i < len; i++)
    {
        char c = input[i];
        if (c == 'Q')
        {
            dp_Q[i] = dp_Q[i-1] + 1;
            dp_QA[i] = dp_QA[i-1];
            dp_QAQ[i] = dp_QA[i] + dp_QAQ[i-1];
        } 
        else if (c == 'A')
        {
            dp_Q[i] = dp_Q[i-1];
            dp_QA[i] = dp_QA[i-1] + dp_Q[i-1];
            dp_QAQ[i] = dp_QAQ[i-1];
        }
        else
        {
            dp_Q[i] = dp_Q[i-1];
            dp_QA[i] = dp_QA[i-1];
            dp_QAQ[i] = dp_QAQ[i-1];
        }
    }

    cout << dp_QAQ[len-1] << endl;
    return 0;
}




/*

        QAQQQZZYNOIWIN
Q       1
QA      0111
QAQ     001

init QA[0] = 0, QAQ[0] = 0




if cur is Q:
    Q[i] = Q[i-1] + 1
    QA[i] = QA[i-1]
    QAQ[i] = QA[i] + QAQ[i-1]
if cur is A:
    Q[i] = Q[i-1]
    QA[i] = QA[i-1] + Q[i-1] 
            number of QA's so far + number of Q's before index i that can be matched with the A in index i
    QAQ[i] = QAQ[i-1]
if neither:
    Q[i] = Q[i-1]
    QA[i] = QA[i-1]
    QAQ[i] = QAQ[i-1]

*/