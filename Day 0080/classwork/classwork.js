const form = document.getElementById("my-form");
const btn = document.getElementById("btn");
const database = [];

function userInfo(){
    const nameValue = form.elements.name.value
    const lsnmValue = form.elements.lsnm.value;
    const emailValue = form.elements.email.value;

    if(nameValue == "" || lsnmValue == "" || emailValue == ""){
        alert("visatyueb erti? !!!!!");
        return;
    }

    const acc = {
        name: nameValue,
        lastname: lsnmValue,
        email: emailValue,
    }

    database.push(acc);
    console.log(database);
}

btn.onclick = userInfo