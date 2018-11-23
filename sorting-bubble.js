function sortBubble(A) {
  const N = A.length;

  for (let r = 1; r < N - 1; r++){
    for (let i = 0; i < N - 1; i++) {
      if (A[i] > A[i+1]) {
        let tmp = A[i+1];
        A[i+1] = A[i];
        A[i] = tmp;
      }
    }
  }

  return A;
}

// Tests
let a = [2,6,1,4,8,10,5];
console.log(sortBubble(a));
