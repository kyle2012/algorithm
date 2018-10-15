class TreeNode {
  constructor(leftNode, rightNode, value, x, y) {
    this.leftNode = leftNode
    this.rightNode = rightNode
    this.value = value
    this.x = x
    this.y = y
  }
}

const transToBinaryTree = (treeNode, arr) => {
  if(!treeNode) {
    return
  }
  let m = treeNode.y
  let n = treeNode.x
  if (m >= arr.length || n >= arr[m].length) {
    return
  }
  treeNode.value = arr[treeNode.y][treeNode.x]
  let hasLeftChild = false
  if(m < arr.length - 1 && n < arr[m].length) {
    leftNode = new TreeNode();
    leftNode.y = m+1
    leftNode.x = n
    treeNode.leftNode = leftNode;
    hasLeftChild = true
  }
  let hasRightChild = false
  if(n < arr[m].length - 1) {
    rightNode = new TreeNode();
    rightNode.y = m
    rightNode.x = n+1
    treeNode.rightNode = rightNode;
    hasRightChild = true
  }
  if(!hasLeftChild && !hasRightChild) {
    return
  }
  if(hasLeftChild) {
    transToBinaryTree(treeNode.leftNode, arr)
  }
  if(hasRightChild) {
    transToBinaryTree(treeNode.rightNode, arr);
  }
}

const traverseTreeNode = (treeNode) => {
  if(!treeNode || !treeNode.value) {
    return
  }
  console.log(treeNode.value)
  traverseTreeNode(treeNode.leftNode)
  traverseTreeNode(treeNode.rightNode)
}

const solve = (treeNode, paths, length, dict) => {
  if(!treeNode || !treeNode.value) {
    return
  }
  paths[length++] = treeNode.value
  if(!treeNode.leftNode && !treeNode.rightNode) {
    calToDict(dict, paths)
  }
  solve(treeNode.leftNode, paths, length, dict)
  solve(treeNode.rightNode, paths, length, dict)
}


const calToDict = (dict, arr) => {
  let sum = 0
  let path = ""
  for(let i=0; i < arr.length; i++) {
    path += arr[i] + "->"
    sum += arr[i]
  }
  path = path.substr(0, path.length - 2)
  dict[sum] = path;
  return dict;
}

const findMinPath = (dict) => {
  let minPath = 90
  for(let key in dict) {
    if(parseInt(key) < minPath) {
      minPath = parseInt(key)
    }
  }
  console.log("The minimum path is: " + dict[minPath+""])
  return dict[minPath+""]
}

let arr = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

let treeNode = new TreeNode(null, null, 0, 0, 0);
transToBinaryTree(treeNode, arr)
//traverseTreeNode(treeNode)
let paths = []
let dict = {}
solve(treeNode, paths, 0, dict)
console.log(dict)
findMinPath(dict)
