# Birr Watch – Live ETB Exchange Rate Tracker

A data‑driven single‑page app that loads live exchange rates for the Ethiopian Birr, converts an amount to a chosen currency, and keeps a persistent watchlist of favourite currencies.

## What it does
- Fetches live rates from a public API on startup.
- Converts any amount from ETB to the selected currency.
- Adds currencies to a watchlist (no duplicates).
- Removes currencies from the watchlist.
- Remembers your watchlist and last chosen currency across page reloads using `localStorage`.
- Shows loading, success and error states.

## Which API it calls
Uses the free, no‑key endpoint: https://open.er-api.com/v6/latest/ETB


## How to open it
1. Save all three files (`index.html`, `styles.css`, `app.js`) in the same folder.
2. open `index.html` in your browser.

## Technologies used
- HTML, CSS, JavaScript