/**
 * Houser rober
 * @see https://leetcode.com/problems/house-robber/
 */

#include <stdio.h>

int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

/**
 * On dynamic programming the idea is to chunk in small problems, so, the first
 * thing was to find the best solution for one, house, after for two, after for
 * three and so on, on paper, this shows a pattern that we can use it as a formula.
 */
int rob(int* nums, int numsSize) {
    int D[1000000];

    if (numsSize == 0) {
        return 0;
    }
    if (numsSize == 1) {
        return nums[0];
    }

    D[0] = nums[0];
    D[1] = max(D[0], nums[1]);
    printf("D%i: %i\n", 0, D[0]);
    printf("D%i: %i\n", 1, D[1]);

    for(int i = 2; i < numsSize; i++) {
        D[i] = max(nums[i] + D[i-2], D[i-1]);
        printf("D%i: %i\n", i, D[i]);
    }

    return D[numsSize - 1];
}

int main() {
  int a[5] = {2,7,9,3,1};

  printf("Max: %i\n", rob(a, 5));
}
