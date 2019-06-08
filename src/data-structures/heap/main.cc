#include "Heap.h"
#include <ctime>
#include <iostream>

using namespace std;

int main() {
    constexpr int N = 10;
    srand(time(NULL));
    int a[N];
    for (int i = 0; i < N; i++)
        a[i] = rand() % 100;
    MyHeap<int> minHeap = MyHeap<int>(a, N);
    auto maxHeap = MyHeap<int, greater<int>>(a, N);

    minHeap.printHeap();
    while (!minHeap.empty())
        cout << minHeap.pop() << " ";
    cout << endl;

    maxHeap.printHeap();
    while (!maxHeap.empty()) {
        cout << maxHeap.pop() << " ";
    }
    cout << endl;
    return 0;
}