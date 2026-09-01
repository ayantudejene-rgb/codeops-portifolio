const customer = {
    name: "Almaz Bekele",
    city: "Addis Ababa",
    balance: 1500
};

for (const [key, value] of Object.entries(customer)) {
    console.log(`${key}: ${value}`);
}
// Output:
// name: Almaz Bekele
// city: Addis Ababa
// balance: 1500