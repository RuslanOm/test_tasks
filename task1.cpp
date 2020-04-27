
using namespace std;

bool isEven(int value){
    return value % 2 == 0;
}

bool isEvenBinary(int value){
    return (value & 1) == 0;
}


int main() {
    int n;
    string st;
    cin >> st;
    char last_digit = st[st.size() - 1];
    cout << isEven(stoi(string({last_digit}))) << "\n";
    cout << isEvenBinary(stoi(st));
    return 0;
}
