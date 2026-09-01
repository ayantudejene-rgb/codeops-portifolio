// Function declaration with default rate
function vat(amount, rate = 0.15) {
    return amount * rate;
}

// Arrow function with implicit return (same logic)
const vatArrow = (amount, rate = 0.15) => amount * rate;

// Test
console.log(vat(1000));        // 150
console.log(vatArrow(1000));   // 150
console.log(vat(1000, 0.07));  // 70