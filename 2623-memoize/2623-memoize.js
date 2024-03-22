/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let map = {}
    return function(...args) {
        const key  = args.toString()
        if(key in map) return map[key]
        else{
            let res = fn(...args)
            map[key] = res
            return res
        }        
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */