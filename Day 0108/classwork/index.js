const promise = fetch('https://jsonplaceholder.typicode.com/todos');

promise
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((eror) => console.log("eror: ", eror));