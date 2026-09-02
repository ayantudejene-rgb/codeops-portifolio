async function getEtbRate() {
    const url = 'https://api.exchangerate.host/latest?base=USD';
    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        return data.rates.ETB;
    } catch (err) {
        console.error('Failed to fetch rate:', err);
        return null;
    }
}

getEtbRate().then(rate => console.log('1 USD =', rate, 'ETB'));