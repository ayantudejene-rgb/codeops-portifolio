# Addis Eats – Manual Test Plan

Run through this test plan after every change. All tests must pass before Day 25 assessment.

## Menu & Data
- [ ] Menu loads with "Loading..." message
- [ ] All 8 dishes display correctly
- [ ] Dishes show name, category, price, spicy indicator
- [ ] Breaking the data URL shows calm error message (test by renaming `menu.json`)

## Search
- [ ] Type "Doro" – shows Doro Wat only
- [ ] Type "vegetarian" – shows Shiro and Beyaynetu
- [ ] Search for "xyzabc" – shows "No dishes found"
- [ ] Clear search – all dishes reappear

## Cart
- [ ] Add Doro Wat – appears in cart with qty 1
- [ ] Add Doro Wat again – qty increments to 2
- [ ] Add Shiro – appears as separate item
- [ ] Remove Doro Wat – removes only that item
- [ ] Empty cart shows "Cart is empty"
- [ ] Cart total updates correctly

## Checkout
- [ ] Empty name – shows error
- [ ] Name "A" (too short) – shows error
- [ ] Phone "123" – shows error
- [ ] Phone "0912345678" – valid
- [ ] Phone "+251912345678" – valid
- [ ] Empty cart – checkout blocked with error
- [ ] Valid order – shows confirmation with total
- [ ] Cart clears after order placed
- [ ] Checkout form resets after order

## Persistence
- [ ] Add items to cart, reload – cart restored
- [ ] Place order, reload – cart is empty

## Responsive & Accessibility
- [ ] Mobile (<800px): single column, menu above cart
- [ ] Desktop (≥800px): menu + cart side by side
- [ ] All interactive elements have focus styles
- [ ] Error messages are clear and specific
- [ ] aria-live on error region

## Console
- [ ] No errors in console during any flow
- [ ] No warnings about deprecated features