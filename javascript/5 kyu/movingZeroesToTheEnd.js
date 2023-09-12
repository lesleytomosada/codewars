// Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

// moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]
// ARRAYSSORTINGALGORITHMS
// Ad
// 10 Traits Employers Look for When Hiring Software Engineers
// Codewars CEO Jake Hoffner breaks down the 10 traits he looks for in software engineers.
// powered by 
// Solution

function moveZeros(arr) {
    let i = 0
    for (let j = 0; j<arr.length; j++){
      if (arr[j] !== 0 ){
        let temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i++
        }
    }
    return arr
  }

  var moveZeros2 = function (arr) {
    var filtedList = arr.filter(function (num){return num !== 0;});
    var zeroList = arr.filter(function (num){return num === 0;});
    return filtedList.concat(zeroList);
  }