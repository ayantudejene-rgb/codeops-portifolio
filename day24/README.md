# Addis Eats – Food Ordering App

A single‑page food ordering app for an Addis Ababa restaurant. Browse the menu, search for dishes, build a cart, and place an order with a validated TeleBirr checkout.

## Features

- Browse menu loaded from `data/menu.json`
- Live search/filter by dish name or category
- Add to cart with quantity increment
- Remove items from cart
- Live ETB total using `reduce()`
- Checkout form with real validation:
  - Name: at least 2 characters
  - Phone: Ethiopian regex (`/^(?:\+251|0)9\d{8}$/`)
  - Cart must not be empty
- Order confirmation with total and delivery area
- Cart persists across reloads (`localStorage`)
- Responsive: single column on mobile, side‑by‑side on desktop
- Semantic HTML with accessible labels
- Refactored code: constants, small functions, guard clauses

## Data Source

Menu data is loaded from `data/menu.json` – a local file containing dish objects.

## How to Run

1. Save all files in this folder structure:
2. Open `index.html` in your browser.

## Technologies Used

- HTML5 (semantic elements, forms)
- CSS3 (Grid, Flexbox, custom properties, mobile‑first)
- Vanilla JavaScript (ES6+)
- Fetch API (async/await)
- localStorage (JSON serialization)
- Regular expressions (phone validation)

## Testing

See `TEST_PLAN.md` for the full manual test plan.

## Project Structure

- `index.html` – semantic markup with header, main, section, aside, footer and checkout form
- `styles.css` – responsive styles with CSS variables
- `script.js` – state, fetch, render, events, validation, persistence
- `data/menu.json` – sample menu data
- `TEST_PLAN.md` – repeatable manual test plan
- `README.md` – project documentation

## State Management

The app follows the **state → render → events → edit state → render** loop:
- `state` holds dishes, cart items, and search term
- `render()` builds the UI from state
- Events update state, call `saveCart()`, then re‑render
- Validation guards against bad input before placing orders

## Accessibility

- `aria-label` on main sections
- `aria-live="polite"` on error region
- Logical heading hierarchy
- Focus styles on interactive elements
- Empty, loading, error, and success states displayed clearly