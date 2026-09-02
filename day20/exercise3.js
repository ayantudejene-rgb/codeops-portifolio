async function testFetch(url) {
    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP ${res.status} – ${res.statusText}`);
        const data = await res.json();
        console.log('Data:', data);
    } catch (err) {
        console.error('Caught error:', err.message);
    }
}

testFetch('https://restcountries.com/v3.1/name/xyzabc');  
testFetch('https://this-domain-does-not-exist.example');  