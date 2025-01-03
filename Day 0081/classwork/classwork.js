// // N1 

// function evenSum(border){
//     let sum = 0
//     for(let i = 0; i <= border; i ++){
//         if(i % 2 == 0){
//             sum += i
//         }
//         return sum
//     }
// }


// // N2

// function reversNum(numbers){
//     for(let i = 0; i <= numbers; i --){
//         console.log(i)
//     }
// }


// // N3

// function evenNum(number){
//     for(let i = 0; i <= number; i+2){
//         console.log(i)
//     }
// }


// // N4

// function generateEven(border){
//     numList = [];
//     for(let i = 0; i <= border; i ++){
//         numList.push(i)
//     }
//     return numList
// }

// function calculateSum(numList){
//     let sum = 0;
//     for(let ii = 0; ii <= numList; ii ++){
//         sum += ii
//     }
//     return sum
// }


// // N5

// let numbersList = []

// for (let i = 0; i < 10; i ++){
//     let valueType = {
//         value: i,
//         type: "",
//     }
//     if (i % 2 === 0){
//         valueType.type = "Even";
//     } else {
//         valueType,type = "Odd"
//     }

//     numbersList.push(valueType);
// }

// console.log(numbersList)


// // N6

let authorised = false;
let count = 3

while (authorised !== true && count > 0){
    const pass = prompt("enter your password");

    if (pass === "irakli123"){
        authorised = true,
        alert("Accses granted")
    } else{
        count--,
        alert("Access denied. You have " + count + " attempts left.")
    }
}

console.log(pass)