/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    new_arr = []
    arr.forEach((elem, index)=>{
        new_arr[index] = fn(elem, index)
    })
    return new_arr
};