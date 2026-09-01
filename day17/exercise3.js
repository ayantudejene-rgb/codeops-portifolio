function discountBy(rate) {
    return (price) => price * (1 - rate);
}

const memberPrice = discountBy(0.10);    // 10% off
const salePrice   = discountBy(0.30);    // 30% off

console.log(memberPrice(1000)); // 900
console.log(salePrice(1000));   // 700