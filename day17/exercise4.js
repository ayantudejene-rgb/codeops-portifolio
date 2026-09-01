function applyToAll(list, fn) {
    const results = [];
    for (const item of list) {
        results.push(fn(item));
    }
    return results;
}

const prices = [200, 450, 1200, 80];
const withVat = applyToAll(prices, p => p * 1.15);

console.log(withVat); // [230, 517.5, 1380, 92]