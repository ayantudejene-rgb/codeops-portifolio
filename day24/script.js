// ----- Constants -----
const STORAGE_KEY = 'addiseats';
const PHONE_REGEX = /^(?:\+251|0)9\d{8}$/;
const FREE_DELIVERY_OVER = 500;
const DELIVERY_FEE = 30;

// ----- DOM References -----
const menuGrid = document.getElementById('menuGrid');
const menuStatus = document.getElementById('menuStatus');
const searchInput = document.getElementById('searchInput');
const cartList = document.getElementById('cartList');
const totalAmount = document.getElementById('totalAmount');
const checkoutForm = document.getElementById('checkoutForm');
const nameInput = document.getElementById('name');
const phoneInput = document.getElementById('phone');
const areaSelect = document.getElementById('area');
const formError = document.getElementById('formError');
const placeOrderBtn = document.getElementById('placeOrderBtn');
const confirmationDiv = document.getElementById('confirmation');
const confirmationMessage = document.getElementById('confirmationMessage');

// ----- State -----
const state = {
    dishes: [],
    cart: [],
    search: ''
};

// ----- Cart Persistence -----
function loadCart() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (raw) {
            const parsed = JSON.parse(raw);
            if (Array.isArray(parsed)) state.cart = parsed;
        }
    } catch {
        // Corrupt data – start fresh
    }
}

function saveCart() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state.cart));
}

// ----- Computed Values -----
function cartTotal() {
    return state.cart.reduce((sum, item) => sum + item.price * item.qty, 0);
}

// ----- Render Functions -----
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
    placeOrderBtn.disabled = state.cart.length === 0;
}

function renderMenu() {
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
}

function render() {
    renderMenu();
    renderCart();
}

// ----- Fetch Menu -----
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
    } catch {
        menuStatus.textContent = 'Could not load the menu. Please refresh.';
        menuStatus.className = 'error';
    }
}

// ----- Event Handlers -----
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
    renderMenu();
}

// ----- Validation -----
function validateOrder(name, phone) {
    if (!name.trim() || name.trim().length < 2) {
        return 'Please enter your full name (at least 2 characters).';
    }
    if (!PHONE_REGEX.test(phone)) {
        return 'Enter a valid Ethiopian phone number (09xxxxxxxx or +2519xxxxxxxx).';
    }
    if (state.cart.length === 0) {
        return 'Your cart is empty. Add some dishes first.';
    }
    return '';
}

// ----- Place Order -----
function placeOrder(name, phone, area) {
    const order = {
        name: name.trim(),
        phone: phone.trim(),
        area,
        items: state.cart,
        total: cartTotal(),
        placedAt: new Date().toISOString()
    };

    state.cart = [];
    saveCart();
    render();

    confirmationMessage.textContent =
        `Order placed for ${order.name} – ${order.total} ETB. Delivery to ${order.area}.`;
    confirmationDiv.classList.remove('hidden');

    // Hide confirmation after 6 seconds
    setTimeout(() => {
        confirmationDiv.classList.add('hidden');
    }, 6000);
}

function handleCheckoutSubmit(e) {
    e.preventDefault();

    // Hide previous confirmation
    confirmationDiv.classList.add('hidden');

    const name = nameInput.value;
    const phone = phoneInput.value;
    const area = areaSelect.value;

    const error = validateOrder(name, phone);
    if (error) {
        formError.textContent = error;
        return;
    }

    formError.textContent = '';
    placeOrder(name, phone, area);
    checkoutForm.reset();
}

// ----- Init -----
function init() {
    loadCart();
    loadMenu();

    // Event listeners
    searchInput.addEventListener('input', handleSearch);
    menuGrid.addEventListener('click', handleMenuClick);
    cartList.addEventListener('click', handleCartClick);
    checkoutForm.addEventListener('submit', handleCheckoutSubmit);
}

init();