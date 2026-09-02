# Addis Eats – Food Ordering App

A single‑page food ordering app for an Addis Ababa restaurant. Browse the menu, search for dishes, add items to your cart, and see a live ETB total – all with persistence across page reloads.

## Features

- Browse a menu loaded from a local JSON file
- Live search/filter by dish name or category
- Add items to cart (increment quantity if already added)
- Remove items from the cart
- Live ETB total computed with `reduce()`
- Cart persists across reloads using `localStorage`
- Responsive layout: single column on mobile, menu + cart side‑by‑side on desktop
- Semantic HTML with accessible labels

## Data Source

Menu data is loaded from `data/menu.json` – a local file containing dish objects with `id`, `name`, `category`, `price`, and `spicy` flag.

## How to Run

1. Save all files in the same folder structure:
2. Open `index.html` in your browser.


## Technologies Used

- HTML
- CSS
- JavaScript

## Project Structure

- `index.html` – semantic markup with header, main, section, aside, footer
- `styles.css` – responsive styles with CSS variables
- `script.js` – state, fetch, render, events, persistence
- `data/menu.json` – sample menu data

## State Management

The app follows the **state → render → events → edit state → render** loop:
- `state` holds dishes, cart items, and search term
- `render()` builds the UI from state
- Events update state, call `saveCart()`, then re‑render

## Accessibility

- `aria-label` on main sections
- Logical heading hierarchy
- Focus styles on interactive elements
- Empty, loading, and error states displayed clearly