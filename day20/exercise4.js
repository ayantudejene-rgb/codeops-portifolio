async function fetchDetails() {
    const listUrl = 'https://restcountries.com/v3.1/all?fields=name,cca2';
    try {
        const res = await fetch(listUrl);
        if (!res.ok) throw new Error('Failed to fetch list');
        const countries = await res.json();

        const firstTwo = countries.slice(0, 2);

        const detailPromises = firstTwo.map(c =>
            fetch(`https://restcountries.com/v3.1/alpha/${c.cca2}`)
                .then(r => r.json())
        );
        const details = await Promise.all(detailPromises);
        console.log('Details:', details);
    } catch (err) {
        console.error('Error:', err);
    }
}

fetchDetails();