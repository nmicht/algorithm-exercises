function sortInsertion(A) {
  const N = A.length;

  for (let i = 1; i <= N - 1; i++) {
    let tmp = A[i];
    let x;
    for (x = i-1; A[x] >= tmp; x--) {
      A[x+1] = A[x];
    }
    A[x+1] = tmp;
  }

  return A;
}

// Tests
let a = [2,6,1,4,8,10,5];
console.log(sortInsertion(a));
