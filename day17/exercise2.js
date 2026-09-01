function makeCounter() {
    let count = 0;                     // private – not accessible from outside

    return function() {
        count += 1;
        return count;
    };
}

// Create two independent counters
const counterA = makeCounter();
const counterB = makeCounter();

console.log(counterA()); // 1
console.log(counterA()); // 2
console.log(counterB()); // 1 (separate closure)
console.log(counterB()); // 2

// Explanation:
// Each call to makeCounter() creates a new lexical environment where 'count' lives.
// The returned inner function closes over that environment, so 'count' persists
// between calls. Outside code cannot see or modify 'count' directly because it is
// not returned – it's private to the closure.