const solveAZ = (x, y) => {
  let arr = new Array();
  for(let i=0; i < y+1; i++) {
    arr[i] = new Array();
    for(let j=0; j < x+1; j++) {
      arr[i][j] = 1
    }
  }
  console.log(arr)
  let m = 1
  while(m < x+1){
    let n = 1
    while(n < y+1){
      arr[m][n] = arr[m-1][n] + arr[m][n-1]
      n++
    }
    m++
  }
  return arr
}

result = solveAZ(3, 3)
console.log(result, result[3][3])
