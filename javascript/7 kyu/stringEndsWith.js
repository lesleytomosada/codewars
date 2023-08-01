// Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

// Examples:

// solution('abc', 'bc') // returns true
// solution('abc', 'd') // returns false


function solution(str, ending){
    const endLength = ending.length
    const strLength = str.length
    if (str.slice(strLength-endLength,strLength) === ending){
      return true
    } else{
      return false
    }
    
  }


  function solution2(str, ending){
    return str.endsWith(ending);
  }