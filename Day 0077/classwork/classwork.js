const user = {
    name: "irakli",
    city: "chxorowku",
    age: 17,
    academy: "GOA",
}

console.log(user)


const one = document.getElementById("my-p")
const second = document.getElementById("your-p")

one.textContent = "irakli"
second.textContent = "giorgi"

function greet(){
    let sayHi = document.getElementById("your-p");
    sayHi.textContent = "hello"
}

function colorchange1(){
    let fun1 = document.getElementById("my-p");
    fun1.style.color = "red"
}

function colorchange2(){
    let fun2 = document.getElementById("my-p");
    fun2.style.color = "yellow";
}

function colorchange3(){
    let fun3 = document.getElementById("my-p");
    fun3.style.color = "blue";
}