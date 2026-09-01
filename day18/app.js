import { VAT, addVat } from './money.js';

const prices = [250, 600, 180];
const withVat = prices.map(addVat);
console.log(withVat); // [287.5, 690, 207]
console.log(`VAT rate is ${VAT * 100}%`);