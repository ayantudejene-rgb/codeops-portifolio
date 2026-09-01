const customer = {
    name: "Almaz Bekele",
    city: "Addis Ababa",
    balance: 1500
};

const { name, city } = customer;

console.log(name); // Almaz Bekele
console.log(city); // Addis Ababa

function greet({ name }) {
    return `Selam ${name}!`;
}

console.log(greet(customer)); // Selam Almaz Bekele!