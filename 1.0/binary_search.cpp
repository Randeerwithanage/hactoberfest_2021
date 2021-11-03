#include <iostream>

int binary_search(int a[], int r, int key) {
    int l = 0;

    while (l <= r) {
        int m = l + (r - l) / 2;
        if (key == a[m])
            return m;
        else if (key < a[m])
            r = m - 1;
        else
            l = m + 1;
    }
    return -1;
}

int main() {
    int n, key;
    std::cout << "Enter size of array: ";
    std::cin >> n;
    std::cout << "Enter array elements: ";

    int* a = new int[n];

    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    std::cout << "Enter search key: ";
    std::cin >> key;

    int res = binary_search(a, n - 1, key);
    if (res != -1)
        std::cout << key << " found at index " << res << std::endl;
    else
        std::cout << key << " not found" << std::endl;

    delete[] a;
    return 0;
}
