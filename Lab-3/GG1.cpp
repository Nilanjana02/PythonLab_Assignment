#include <iostream>
#include <vector>

void frequencyCount(std::vector<int>& arr, int n) 
{
    // Step 1: Encode frequencies
    for (int i = 0; i<sizeof(arr); ++i) {
        if (arr[i] <= n) {
            // Increment the position (arr[arr[i] - 1]) by n+1 to mark the frequency count
            arr[arr[i] - 1] += n + 1;
        }
    }

    // Step 2: Decode frequencies
    for (int i = 0; i < n; ++i) {
        // Divide by n+1 to get the actual frequency count
        arr[i] /= (n + 1);
    }
}

int main() {
    // Test cases
    std::vector<int> arr1 = {2, 3, 2, 3, 5};
    int n1 = 5, p1 = 5;
    frequencyCount(arr1, n1, p1);
    for (int num : arr1) {
        std::cout << num << " ";
    }
    std::cout << std::endl; // Output: 0 2 2 0 1

    std::vector<int> arr2 = {3, 3, 3, 3};
    int n2 = 4, p2 = 3;
    frequencyCount(arr2, n2, p2);
    for (int num : arr2) {
        std::cout << num << " ";
    }
    std::cout << std::endl; // Output: 0 0 4 0

    std::vector<int> arr3 = {8, 9};
    int n3 = 2, p3 = 9;
    frequencyCount(arr3, n3, p3);
    for (int num : arr3) {
        std::cout << num << " ";
    }
    std::cout << std::endl; // Output: 0 0

    return 0;
}
