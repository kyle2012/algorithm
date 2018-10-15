const buildMaxHeapify = (arr, i, size) => {
  let largestIndex = i
  let leftIndex = 2*i + 1
  let rightIndex = 2*i + 2
  if(leftIndex < size && arr[largestIndex] > arr[leftIndex]) {
    largestIndex = leftIndex
  }
  if(rightIndex < size && arr[largestIndex] > arr[rightIndex]) {
    largestIndex = rightIndex
  }

  if(largestIndex !== i) {
    let tmp = arr[i]
    arr[i] = arr[largestIndex]
    arr[largestIndex] = tmp
    buildMaxHeapify(arr, largestIndex, size)
  }
}
const kthLargest = (arr, size) => {
  for(let i = size - 1; i >= 0; i--) {
    buildMaxHeapify(arr, i, size)
  }
  for(let i = size; i < arr.length; i++) {
    let tmp = arr[0]
    if(arr[i] > tmp) {
      arr[0] = arr[i]
      arr[i] = tmp
      buildMaxHeapify(arr, 0, size)
    }
  }
  console.log(size + "'th largest is", arr[0])
}

const heapSort = (arr) => {
  for(let i = arr.length - 1; i >= 0; i--) {
    buildMaxHeapify(arr, i, arr.length)
  }
  for(let i = arr.length - 1; i >= 0; i--) {
    let tmp = arr[0]
    arr[0] = arr[i]
    arr[i] = tmp
    buildMaxHeapify(arr, 0, i)
  }
  console.log(arr)
}

let arr = [3,6,2,2,1,4,3,5]
kthLargest(arr, 3)
heapSort(arr)
