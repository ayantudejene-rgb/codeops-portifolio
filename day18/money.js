export const VAT = 0.15;

export function addVat(amount) {
    return amount * (1 + VAT);
}