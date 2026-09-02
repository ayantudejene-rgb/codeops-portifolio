'use strict';

const form = document.querySelector('#searchForm');
const input = document.querySelector('#countryInput');
const factsContainer = document.querySelector('#facts');

async function showCountry(name) {
    factsContainer.innerHTML = '<p class="loading">Loading...</p>';

    try {
        const url = `https://restcountries.com/v3.1/name/${encodeURIComponent(name)}`;
        const res = await fetch(url);

        if (!res.ok) {
            if (res.status === 404) {
                throw new Error('Country not found');
            }
            throw new Error(`HTTP ${res.status} – ${res.statusText}`);
        }

        const data = await res.json();
        const country = data[0];

        const facts = [
            { label: 'Capital', value: country.capital?.[0] || 'N/A' },
            { label: 'Population', value: country.population.toLocaleString() },
            { label: 'Region', value: country.region || 'N/A' },
            { label: 'Currencies', value: country.currencies
                ? Object.values(country.currencies).map(c => c.name).join(', ')
                : 'N/A' }
        ];

        const flag = country.flags?.svg || country.flags?.png || '';

        let html = '';
        if (flag) {
            html += `<div class="flag"><img src="${flag}" alt="Flag of ${country.name.common}" style="max-width:120px;"></div>`;
        }
        facts.forEach(f => {
            html += `
                <div class="fact-item">
                    <span class="fact-label">${f.label}</span>
                    <span class="fact-value">${f.value}</span>
                </div>
            `;
        });
        factsContainer.innerHTML = html;

    } catch (err) {
        // Error state – friendly message
        factsContainer.innerHTML = `<p class="error">⚠️ ${err.message}</p>`;
    }
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = input.value.trim();
    if (name) {
        showCountry(name);
    }
});

showCountry('ethiopia');