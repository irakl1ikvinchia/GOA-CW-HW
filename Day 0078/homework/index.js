const form = document.getElementById("passForm");
const btn = document.getElementById("btn");

function passCheck(){
    const resPass = form.elements.pass.value;
    
    if(resPass.length < 8){
        alert("this password incorect");
        return;
    }

    console.log("password is good ✅")
    console.log("password: " + resPass)
}

btn.onclick = passCheck