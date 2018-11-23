function sortSelection(A) {
  const N = A.length;

  for (let i = 0; i < N-1; i++) {
    iMin = findPosMin(A, i);
    tmp = A[iMin];
    A[iMin] = A[i];
    A[i] = tmp;
  }

  return A;
}

function findPosMin(A, i) {
  let min = A[i];
  let minPos = i;

  for(let j = i; j < A.length; j++) {
    if(A[j] < min) {
      min = A[j];
      minPos = j;
    }
  }
  return minPos;
}

// Tests
let a = [2,6,1,4,8,10,5];
console.log(sortSelection(a));
