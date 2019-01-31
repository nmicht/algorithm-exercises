// Majority Element
// https://leetcode.com/problems/majority-element/

// Solution using: Boyer–Moore majority vote algorithm
// https://en.m.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

int majorityElement(int* nums, int numsSize) {
    int majorityNumber = nums[0];
    int majorityCounter = 1;

    for(int i=1; i<numsSize; i++) {
        if(majorityCounter == 0){
            majorityNumber = nums[i];
            majorityCounter++;
        } else if(nums[i] == majorityNumber) {
            majorityCounter++;
        } else {
            majorityCounter--;
        }
    }

    return majorityNumber;
}
