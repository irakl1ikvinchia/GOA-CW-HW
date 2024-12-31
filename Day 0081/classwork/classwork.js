// N1 

function evenSum(border){
    let sum = 0
    for(let i = 0; i <= border; i ++){
        if(i % 2 == 0){
            sum += i
        }
        return sum
    }
}


// N2

function reversNum(numbers){
    for(let i = 0; i <= numbers; i --){
        console.log(i)
    }
}


// N3

function evenNum(number){
    for(let i = 0; i <= number; i+2){
        console.log(i)
    }
}


// N4

function generateEven(border){
    numList = [];
    for(let i = 0; i <= border; i ++){
        numList.push(i)
    }
}

function calculateSum(numList){
    let sum = 0;
    for(let ii = 0; ii <= numList; ii ++){
        sum += ii
    }
    return sum
}


// N5

