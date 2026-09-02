const PHONE = /^(?:\+251|0)9\d{8}$/;

const form = document.getElementById('signupForm');
const nameInput = document.getElementById('name');
const phoneInput = document.getElementById('phone');
const errorMsg = document.getElementById('errorMsg');
const countDisplay = document.getElementById('countDisplay');

function validate(name, phone) {
    if (name.trim().length < 2) return 'Please enter your full name (at least 2 characters).';
    if (!PHONE.test(phone)) return 'Enter a valid Ethiopian phone number (09xxxxxxxx or +2519xxxxxxxx).';
    return '';
}

function loadEntries() {
    try {
        const raw = localStorage.getItem('signups');
        return raw ? JSON.parse(raw) : [];
    } catch {
        return [];
    }
}

function saveEntries(entries) {
    localStorage.setItem('signups', JSON.stringify(entries));
}

function updateCount() {
    const entries = loadEntries();
    countDisplay.textContent = `Total signups: ${entries.length}`;
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = nameInput.value.trim();
    const phone = phoneInput.value.trim();
    const error = validate(name, phone);
    if (error) {
        errorMsg.textContent = error;
        return;
    }
    errorMsg.textContent = '';
    const entries = loadEntries();
    entries.push({ name, phone });
    saveEntries(entries);
    form.reset();
    updateCount();
});

updateCount();