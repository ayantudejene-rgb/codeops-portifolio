const customer = {
    name: "Almaz Bekele",
    city: "Addis Ababa",
    balance: 1500
};

const updatedCustomer = {
    ...customer,
    city: "Bahir Dar",
    phone: "0911-123456"
};

console.log(customer);
console.log(updatedCustomer);
