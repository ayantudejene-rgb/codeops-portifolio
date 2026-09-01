import { transactions } from './transactions.js';
import { totalByType, formatReceipt, buildReceipts } from './report.js';

// 1. Totals by type
const totalDebit = totalByType(transactions, 'debit');
const totalCredit = totalByType(transactions, 'credit');

console.log(`Total debits: ${totalDebit} ETB`);
console.log(`Total credits: ${totalCredit} ETB`);

// 2. Receipt strings (using map with destructuring)
const receipts = buildReceipts(transactions);
receipts.forEach(r => console.log(r));

// 3. Spread to update a transaction
const original = transactions[0]; 
const corrected = { ...original, amount: 300 }; // change amount to 300

console.log('Original:', original);
console.log('Corrected:', corrected);