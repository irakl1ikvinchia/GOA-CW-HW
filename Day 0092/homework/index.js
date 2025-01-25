const form = document.querySelector("form");
const ul = document.getElementById("itemList");

const index = 0;

form.addEventListener("click", (e) => {
    e.preventDefault();

    const item = form.item.value;
    ul.innerHTML += `<li id=${index}>${item}</li>`;
    index++;

    form.item.value = "";
})

ul.addEventListener("click", (e) => {
    if (e.target.tagName === "LI"){
        e.target.remove();
    }
})

