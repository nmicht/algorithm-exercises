/*
 Single number
 https://leetcode.com/problems/single-number/
 */

#include<limits.h>
#include<stdio.h>

#define MAX_SIZE = 100000;

int singleNumber(int* nums, int numsSize) {

    int freqPos[MAX_SIZE] = {0};
    int freqNeg[MAX_SIZE] = {0};

    for(int i=0; i<numsSize; i++) {
        int currentNumber = abs(nums[i]);
        if(nums[i] < 0) {
            if(freqNeg[currentNumber] == 0){
                freqNeg[currentNumber] = 1;
            } else {
                freqNeg[currentNumber] = 0;
            }
        } else if(freqPos[currentNumber] == 0){
            freqPos[currentNumber] = 1;
        } else {
            freqPos[currentNumber] = 0;
        }
    }

    for(int j=0; j<MAX_SIZE; j++){
        if(freqPos[j] != 0) {
            return j;
        }
        if(freqNeg[j] != 0){
            return -j;
        }
    }

    return -1;
}
