/**
 * SOLVED
 * https://www.interviewbit.com/problems/wave-array/
 *
 */
 module.exports = {
  //param A : array of integers
  //return a array of integers
     wave : function(A){
         A = A.sort(function(a, b) {
           return a - b;
         });
         for (i = 0; i < A.length - 1; i++) {
             if( i%2 == 0 && A[i] < A[i+1]) {
                 temp = A[i]
                 A[i] = A[i+1]
                 A[i+1] = temp
             }
             else if( i%2 != 0 && A[i] > A[i+1]) {
                 temp = A[i]
                 A[i] = A[i+1]
                 A[i+1] = temp
             }
         }
         return A
     }
 };
