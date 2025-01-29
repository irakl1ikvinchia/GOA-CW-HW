const form = document.querySelector("form");
const accounts = [];

class Account {
    constructor(firstName, lastName, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
    }

    printDetails() {
        console.log(`firstName: ${this.firstName}`);
        console.log(`lastName: ${this.lastName}`);
        console.log(`email: ${this.email}`);
    }
}

form.addEventListener('click', (e) => {
    e.preventDefault();

    const firstName = form.firstName.value;
    const lastName = form.lastName.value;
    const email = form.email.value;

    const account = new Account(firstName, lastName, email);
    account.printDetails();
    console.log(account)
    accounts.push(account)
})