// Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/
#include<stdio.h>

void xor(int** A, int indexRow, int indexColumn, int size) {
    if (indexRow != -1) {
        for (int c = 0; c < size; c++) {
            A[indexRow][c] = A[indexRow][c]^1;
        }
    } else if (indexColumn != -1) {
        for (int r = 0; r < size; r++) {
            A[r][indexColumn] = A[r][indexColumn]^1;
        }
    }
}

int haveZeroMajority(int** A, int indexColumn, int size) {
    int sum = 0;

    for (int i = 0; i < size; i++) {
        sum += A[i][indexColumn];
    }

    if (sum > (size/2 + size%2)) {
        return 0;
    } else {
        return 1;
    }
}

int sum(int** A, int ARowSize, int AColSizes) {
  int sum = 0;
  for(int r = 0; r < ARowSize; r++) {
    int number = 0;
    for(int c = AColSizes-1, y = 0; c >= 0; c--, y++) {
      number += A[r][c] * pow(2,y);
    }
    sum += number;
  }
  return sum;
}

int matrixScore(int** A, int ARowSize, int* AColSizes) {
    // Change the mostleft to 1
    for(int r = 0; r < ARowSize; r++) {
        if(A[r][0] == 0) {
            xor(A, r, -1, AColSizes[0]);
        }
    }

    // For each column, if the majority is for 0, change to 1
    for (int c = 1; c < AColSizes[0]; c++) {
        if(haveZeroMajority(A, c, ARowSize)) {
            xor(A, -1, c, ARowSize);
        }
    }

    // Get the matrix sum
    return sum(A, ARowSize, AColSizes[0]);
}

void print(int** A) {
  for(int r = 0; r < 3; r++) {
    for(int c = 0; c < 4; c++) {
      printf("%i\t", A[r][c]);
    }
    printf("\n");
  }
}

void main() {
  // int matrix[3][4] = {{0,0,1,1},{1,0,1,0},{1,1,0,0}};

  // print(matrix);
  // matrixScore(*matrix, 3, *colSize);
  // print(*matrix);

}
