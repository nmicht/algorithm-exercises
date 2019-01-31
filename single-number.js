// Single number
// https://leetcode.com/problems/single-number/

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  let value;

  for (i of nums) {
    value = value ^ i;
  }

  return value;
};
