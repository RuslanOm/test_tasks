#include <bits/stdc++.h>


using namespace std;


template<class T>
class RingBufferArray {
public:
    int max_size, tail, head, true_size;
private:
    vector<T> data;

public:

    RingBufferArray(int max_size) {
        data.resize(max_size);
        this->max_size = max_size;
        this->true_size = 0;
        this->head = 0;
        this->tail = 0;
    }

    void append(T x) {
        data[tail % max_size] = x;
        tail++;
        if (tail % max_size == head % max_size) {
            head++;
        }
        if (true_size < max_size) {
            true_size++;
        }
    }

    T pop() {
        if (true_size > 0) {
            int ind = head % max_size - 1;
            if (ind < 0)
                ind = max_size - 1;
            T val = data[ind];
            data[ind] = -1;
            head++;
            true_size--;
            if (true_size == 0) {
                head = 0;
                tail = 0;
            }
            return val;
        } else {
            throw out_of_range("Pop from empty buffer");
        }
    }

    int size() {
        return true_size;
    }
};

template<class T>
class RingBufferDeq {
public:
    int max_size;
private:
    deque<T> data;
public:
    RingBufferDeq(int max_size) {
        this->max_size = max_size;
    }

    void append(T x) {
        if (data.size() >= max_size) {
            data.pop_front();
            data.push_back(x);
        } else {
            data.push_back(x);
        }
    }

    T pop() {
        if (!data.empty()) {
            T val = data.front();
            data.pop_front();
            return val;
        } else {
            throw out_of_range("Pop from empty buffer");
        }
    }

    int size() {
        return data.size();
    }
};


int main() {
// some test code
    RingBufferArray<int> rba(10);
    for (int i = 0; i < 15; ++i) {
        rba.append(i);
    }
    cout << "Array buffer\n";
    for (int j = 0; j < 10; ++j) {
        cout << rba.pop() << "\n";
    }
    cout << "\n";
    RingBufferDeq<int> rbq(10);
    for (int i = 0; i < 15; ++i) {
        rbq.append(i);
    }
    cout << "Deque buffer\n";
    for (int j = 0; j < 10; ++j) {
        cout << rbq.pop() << "\n";
    }
    return 0;
}
