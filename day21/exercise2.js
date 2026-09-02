function saveArray(key, arr) {
    localStorage.setItem(key, JSON.stringify(arr));
}

function loadArray(key) {
    try {
        const raw = localStorage.getItem(key);
        return raw ? JSON.parse(raw) : [];
    } catch {
        return [];
    }
}