export function totalByType(transactions, type) {
    return transactions
        .filter(t => t.type === type)
        .reduce((sum, { amount }) => sum + amount, 0);
}

export function formatReceipt(transaction) {
    const { customer, amount, type } = transaction;
    return `${customer} ${type === 'credit' ? 'received' : 'paid'} ${amount} ETB`;
}

export function buildReceipts(transactions) {
    return transactions.map(({ customer, amount, type }) =>
        `${customer} ${type === 'credit' ? 'received' : 'paid'} ${amount} ETB`
    );
}