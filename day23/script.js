const state = {
    dishes: [],
    cart: [],
    search: ''
};

const menuGrid = document.getElementById('menuGrid');
const menuStatus = document.getElementById('menuStatus');
const searchInput = document.getElementById('searchInput');
const cartList = document.getElementById('cartList');
const totalAmount = document.getElementById('totalAmount');
const checkoutBtn = document.getElementById('checkoutBtn');
const STORAGE_KEY = 'addiseats';

function loadCart() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (raw) {
            const parsed = JSON.parse(raw);
            if (Array.isArray(parsed)) state.cart = parsed;
        }
    } catch {}
}

function saveCart() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state.cart));
}

function cartTotal() {
    return state.cart.reduce((sum, item) => sum + item.price * item.qty, 0);
}

function renderCart() {
    if (state.cart.length === 0) {
        cartList.innerHTML = '<li class="empty-cart">Cart is empty</li>';
    } else {
        cartList.innerHTML = state.cart
            .map(item => `
                <li data-id="${item.id}">
                    <div class="item-info">
                        <span class="item-name">${item.name}</span>
                        <span class="item-qty">×${item.qty}</span>
                    </div>
                    <div>
                        <span class="item-price">${item.price * item.qty} ETB</span>
                        <button class="remove-btn" data-action="remove">✕</button>
                    </div>
                </li>
            `)
            .join('');
    }
    totalAmount.textContent = cartTotal();
    checkoutBtn.disabled = state.cart.length === 0;
}

function render() {
    const term = state.search.toLowerCase().trim();
    const filtered = state.dishes.filter(d =>
        d.name.toLowerCase().includes(term) ||
        d.category.toLowerCase().includes(term)
    );

    if (filtered.length === 0) {
        menuGrid.innerHTML = '<p class="empty-msg">No dishes found. Try a different search.</p>';
    } else {
        menuGrid.innerHTML = filtered
            .map(d => `
                <article class="dish-card" data-id="${d.id}">
                    <h3>${d.name}</h3>
                    <span class="category">${d.category} ${d.spicy ? '🌶️' : ''}</span>
                    <span class="price">${d.price} ETB</span>
                    <button class="add-btn" data-action="add">Add to cart</button>
                </article>
            `)
            .join('');
    }

    renderCart();
}

async function loadMenu() {
    menuStatus.textContent = 'Loading menu...';
    menuStatus.className = 'loading';
    try {
        const res = await fetch('data/menu.json');
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        state.dishes = await res.json();
        menuStatus.textContent = '';
        menuStatus.className = '';
        render();
    } catch (err) {
        menuStatus.textContent = 'Could not load the menu. Please refresh.';
        menuStatus.className = 'error';
    }
}

function handleMenuClick(e) {
    const target = e.target;
    if (!target.matches('[data-action="add"]')) return;

    const card = target.closest('.dish-card');
    if (!card) return;

    const id = Number(card.dataset.id);
    const dish = state.dishes.find(d => d.id === id);
    if (!dish) return;

    const existing = state.cart.find(item => item.id === id);
    if (existing) {
        existing.qty += 1;
    } else {
        state.cart.push({ ...dish, qty: 1 });
    }

    saveCart();
    render();
}

function handleCartClick(e) {
    const target = e.target;
    if (!target.matches('[data-action="remove"]')) return;

    const li = target.closest('li');
    if (!li) return;

    const id = Number(li.dataset.id);
    state.cart = state.cart.filter(item => item.id !== id);
    saveCart();
    render();
}

function handleSearch(e) {
    state.search = e.target.value;
    render();
}

searchInput.addEventListener('input', handleSearch);
menuGrid.addEventListener('click', handleMenuClick);
cartList.addEventListener('click', handleCartClick);

function init() {
    loadCart();
    loadMenu();
}

init();