#include<iostream>
#include<vector>
using namespace std;

 vector<int> passedBy(int a, int &b) {
        // code here
        vector <int> v;
        v[0] = a+1;
        v[1] = b+2;
        return v;
    }