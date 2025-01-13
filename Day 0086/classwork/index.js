// N1

console.log(Math.round(3.4))
console.log(Math.floor(3.7))
console.log(Math.trunc(3.5))
console.log(Math.ceil(3.2))
console.log(Math.sign(2))
console.log(Math.pow(5, 2))
console.log(Math.sqrt(25))
console.log(Math.cbrt(8))
console.log(Math.trunc(Math.random() * 10))

const d = new Date();

console.log(d)


// N2

time = 10;

const bob = setInterval(function() {
    time--;
    console.log(time);
    if (time === 0){
        clearInterval(bob)
        console.log("Time up")
    }
}, 1000)


// N3
// შექმენით ინეტრვალი, გადაცემულ ფუნციაში ყოველ ჯერზე შექმენით date ობიექტი, 
// როცა ამჟამინდელი წუთი გაუტოლდება 35, უნდა გაითიშოს ინეტრვალი

time = 0;

const bo = setInterval(function() {
    time++;
    console.log(time);
    if (time === 35){
        clearInterval(bo)
        console.log("Time up")
    }
}, 1000)