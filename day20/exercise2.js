async function fetchAndRender() {
    try {
        const res = await fetch('https://restcountries.com/v3.1/name/ethiopia');
        const data = await res.json();
        render(data);
    } catch (err) {
        console.error(err);
    }
}