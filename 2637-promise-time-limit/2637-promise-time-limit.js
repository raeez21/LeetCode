/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    
    return async function(...args) {
        const originalPromise = fn(...args)
        const timePromise = new Promise((res,rej)=>{
            setTimeout(rej,t,'Time Limit Exceeded')
        })
        
        return Promise.race([originalPromise, timePromise])
    }   
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */