const form = document.getElementById("my-form")
const btn = document.getElementById("btn")

function userInfo(){
    const nameValue = form.elements.name.value;
    const emailValue = form.elements.email.value;
    const passwordValue = form.elements.password.value;
    const colorValue = form.elements.color.value;

    if (nameValue == "" || emailValue == "" || passwordValue == "" || colorValue == ""){
        alert("please fill in all filed");
        return 
    }

    alert("form submit successfully");
    console.log("form submit successfully")
    console.log("name: " + nameValue);
    console.log("email: " + emailValue);
    console.log("password: " + passwordValue);
    console.log("favColor: " + colorValue)
}


btn.onclick = userInfo