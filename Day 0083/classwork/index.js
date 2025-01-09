const form = document.getElementById("my_form");
const database = [];

function Accaunt(name, lastname, email){
    this.name = name;
    this.lastname = lastname;
    this.email = email;
}

form.addEventListener("submit", function(e){
    e.preventDefault();

    const name = form.name.value;
    const lastname = form.lastname.value;
    const email = form.email.value;

    const acc = new Accaunt(name, lastname, email);
    database.push(acc);

    console.log(database);
})