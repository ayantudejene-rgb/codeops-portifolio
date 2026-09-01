const prices = [250, 600, 180, 900, 1200, 450];

const result = prices
    .map(p => p * 1.15)              // add 15% VAT
    .filter(p => p < 1000)           // keep under 1000
    .reduce((sum, p) => sum + p, 0); // grand total

console.log(result); 

console.log(result); // 1702