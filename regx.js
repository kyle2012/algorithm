const match = (str, pattern) => {
  let i = 0, j = 0;
  return matchRecursive(i, j, str, pattern)
}

const matchRecursive = (i, j, str, pattern) => {
  if( i >= str.length - 1) {
    return true;
  }
  if(pattern.charAt(i) === '*') {
    i++;
    j++;
    if(j >= pattern.length - 1 ) {
      return true;
    }
    matched = matchRecursive(i, j, str, pattern)
    while(!matched) {
      i++;
      matched = matchRecursive(i, j, str, pattern)
    }
    return matched;
  } else if(pattern.charAt(j) === "." || str.charAt(i) === pattern.charAt(j)) {
    i++;
    j++;
    return matchRecursive(i, j, str, pattern)
  } else {
    return false;
  }
}

result = match("abccca", "a.*cca")
console.log(result)
