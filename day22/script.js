const API = 'https://open.er-api.com/v6/latest/ETB';
const STORAGE_KEY = 'birrwatch';

const statusEl = document.getElementById('status');
const convertForm = document.getElementById('convertForm');
const amountInput = document.getElementById('amount');
const currencySelect = document.getElementById('currency');
const resultEl = document.getElementById('result');
const watchlistUl = document.getElementById('watchlist');
const addCurrencyInput = document.getElementById('addCurrency');
const addWatchlistBtn = document.getElementById('addWatchlistBtn');

const state = {
    base: 'ETB',
    rates: {},
    watchlist: [],
    currency: 'USD'
};

function loadSaved() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (raw) {
            const saved = JSON.parse(raw);
            if (saved.watchlist) state.watchlist = saved.watchlist;
            if (saved.currency) state.currency = saved.currency;
        }
    } catch {}
}

function saveState() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
        watchlist: state.watchlist,
        currency: state.currency
    }));
}

async function loadRates() {
    statusEl.textContent = 'Loading rates...';
    statusEl.className = 'loading';
    try {
        const res = await fetch(API);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        state.rates = data.rates;
        statusEl.textContent = '';
        statusEl.className = '';
        render();
    } catch (err) {
        statusEl.textContent = 'Could not load rates. Try again later.';
        statusEl.className = 'error';
        state.rates = {};
        render();
    }
}

function renderCurrencyOptions() {
    const codes = Object.keys(state.rates);
    currencySelect.innerHTML = codes
        .map(code => `<option value="${code}">${code}</option>`)
        .join('');
    currencySelect.value = state.currency;
}

function renderWatchlist() {
    if (state.watchlist.length === 0) {
        watchlistUl.innerHTML = '<li class="empty-msg">No currencies yet</li>';
        return;
    }
    watchlistUl.innerHTML = state.watchlist
        .map(code => {
            const rate = state.rates[code];
            const rateDisplay = rate ? rate.toFixed(4) : '?';
            return `<li data-c="${code}">
                1 ETB = ${rateDisplay} ${code}
                <button class="remove-btn" data-action="remove">×</button>
            </li>`;
        })
        .join('');
}

function render() {
    renderCurrencyOptions();
    renderWatchlist();
}

function handleConvert(e) {
    e.preventDefault();
    const amount = Number(amountInput.value);
    if (!amount || amount <= 0) {
        resultEl.textContent = 'Enter a valid positive amount.';
        return;
    }
    const target = state.currency;
    const rate = state.rates[target];
    if (!rate) {
        resultEl.textContent = 'Selected currency not available.';
        return;
    }
    const converted = (amount * rate).toFixed(2);
    resultEl.textContent = `${amount} ETB = ${converted} ${target}`;
    state.currency = target;
    saveState();
}

function handleAddWatchlist() {
    const code = addCurrencyInput.value.trim().toUpperCase();
    if (!code) return;
    if (!state.rates[code]) {
        alert('Currency code not found in rates.');
        return;
    }
    if (state.watchlist.includes(code)) {
        alert('Already in watchlist.');
        return;
    }
    state.watchlist.push(code);
    saveState();
    renderWatchlist();
    addCurrencyInput.value = '';
}

function handleWatchlistClick(e) {
    const target = e.target;
    if (target.matches('[data-action="remove"]')) {
        const li = target.closest('li');
        const code = li.dataset.c;
        if (code) {
            state.watchlist = state.watchlist.filter(c => c !== code);
            saveState();
            renderWatchlist();
        }
    }
}

convertForm.addEventListener('submit', handleConvert);
addWatchlistBtn.addEventListener('click', handleAddWatchlist);
watchlistUl.addEventListener('click', handleWatchlistClick);

function init() {
    loadSaved();
    loadRates();
}

init();