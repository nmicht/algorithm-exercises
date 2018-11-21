/*
Spiral Order Matrix

Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:

Given the following matrix:

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

You should return

[1, 2, 3, 6, 9, 8, 7, 4, 5]
*/

function spiralOrder(A){
    const B = [];
    const R = A.length;
    const C = A[0].length;
    let top = 0;
    let right = C - 1;
    let left = 0;
    let bottom = R - 1;
    let i = 0;
    let dir = 0; // 0 right, 1 down, 2 left, 3 up

    while(top <= bottom && left <= right) {
      if (dir === 0) {
        for (i = left; i <= right; i += 1) {
          B.push(A[top][i]);
        }
        top += 1;
      }
      else if (dir === 1) {
        for (i = top; i <= bottom; i += 1) {
          B.push(A[i][right]);
        }
        right -= 1;
      }
      else if (dir === 2) {
        for (i = right; i >= left; i -= 1) {
          B.push(A[bottom][i]);
        }
        bottom -= 1;
      }
      else if (dir === 3) {
        for (i = bottom; i >= top; i -= 1) {
          B.push(A[i][left])
        }
        left += 1;
      }
      dir = (dir+1)%4;
    }
    return B;
}

// Tests
let a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]];
console.log(spiralOrder(a));
