'use strict';


const form = document.querySelector('#addForm');
const nameInput = document.querySelector('#itemName');
const priceInput = document.querySelector('#itemPrice');
const list = document.querySelector('#shoppingList');
const totalEl = document.querySelector('#totalAmount');


function updateTotal() {
    const items = list.querySelectorAll('li');
    let total = 0;
    for (const li of items) {
        const priceSpan = li.querySelector('.price');
        if (priceSpan) {
            total += Number(priceSpan.textContent);
        }
    }
    totalEl.textContent = total;
}


function addRow(name, price) {
    const li = document.createElement('li');

    
    const textSpan = document.createElement('span');
    textSpan.textContent = name;

    const priceSpan = document.createElement('span');
    priceSpan.className = 'price';
    priceSpan.textContent = price;

    
    const delBtn = document.createElement('button');
    delBtn.className = 'del-btn';
    delBtn.textContent = '✕';


    li.append(textSpan);
    li.append(priceSpan);
    li.append(delBtn);
    list.append(li);
}


form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = nameInput.value.trim();
    const price = Number(priceInput.value);
    if (!name || !price || price <= 0) return;
    addRow(name, price);
    form.reset();
    updateTotal();
});


list.addEventListener('click', (e) => {
    const target = e.target;


    if (target.matches('.del-btn')) {
        target.closest('li').remove();
        updateTotal();
        return;
    }

    const li = target.closest('li');
    if (li) {
        li.classList.toggle('bought');
    }
});

updateTotal();