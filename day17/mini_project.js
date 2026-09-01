'use strict';
function createLoyalty(earnRule = (etb) => Math.floor(etb / 10)) {
    let points = 0;      
    const addPoints = (amount) => earnRule(amount);
    const canRedeem = (requested) => points >= requested;

    return {
        earn(amount) {
            const earned = addPoints(amount);
            points += earned;
            return earned; 
        },

        redeem(requested) {
            if (canRedeem(requested)) {
                points -= requested;
                return true;
            } else {
                return false;
            }
        },

        balance() {
            return points;
        }
    };
}

//  1 point per 10 ETB
const normalCard = createLoyalty();
normalCard.earn(250);   // +25 points
normalCard.earn(80);    // +8 points  (80/10 = 8)
console.log('Normal card balance:', normalCard.balance()); // 33

normalCard.redeem(10);  // success
console.log('After redeeming 10:', normalCard.balance()); // 23

normalCard.redeem(100); // insufficient – balance stays 23
console.log('After attempting to redeem 100:', normalCard.balance()); // 23

// 2. double points (2 points per 10 ETB)
const holidayRule = (etb) => Math.floor(etb / 10) * 2;
const holidayCard = createLoyalty(holidayRule);
holidayCard.earn(250);   // +50 points (25*2)
holidayCard.earn(80);    // +16 points (8*2)
console.log('Holiday card balance:', holidayCard.balance()); // 66

// 3. Ensure cards are independent
console.log('Normal card balance remains:', normalCard.balance()); // still 23

// Explanation
// The points variable is declared inside createLoyalty and is not returned.
// It is captured by the inner functions (earn, redeem, balance) via closure.
// Outside code cannot read or write 'points' directly – it must go through the
// returned interface. This makes the state truly private.