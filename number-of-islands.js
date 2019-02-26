/**
 * @param {character[][]} grid
 * @return {number}
 * [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
 * [["1","1","1"],["0","1","0"],["1","1","1"]]
 */
var numIslands = function(grid) {
    let isle = 0
    for(let r = 0; r < grid.length; r++) {
        for(let c = 0; c < grid[0].length; c++) {
            console.log(`For position [${r}][${c}]: ${grid[r][c]}`);
            if (grid[r][c] === "1" &&
                grid[r][c-1] !== "1" && // left
                grid[r][c+1] !== "1" && // right
                (r>0 && grid[r-1][c] !== "1") && // top
                grid[r+1][c] !== "1"  // bottom
            ) {
                console.log(' increase island');
                isle++;
            }
        }
    }
    return isle;
};

(() => {
  const grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]];
  let r = numIslands(grid);
  console.log(r);
})();
