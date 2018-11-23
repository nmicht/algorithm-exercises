function sortInsertion(A) {
  const N = A.length;

  let boundary = 0;

  for (let i = boundary + 1; i <= N -1; i++) {  // N-2
    for (let j = 0; j <= boundary; j++) { //
      if (A[j] > A[i]) {
        insertBefore(A, i, j);
        break;
      }
    }
    boundary++;
  }

  return A;
}

function insertBefore(A, i, j){
  let tmp = A[i];
  for (let x = i-1; x >= j; x--) {
    A[x+1] = A[x];
  }
  A[j] = tmp;
}

// Tests
let a = [2,6,1,4,8,10,5];
console.log(sortInsertion(a));
