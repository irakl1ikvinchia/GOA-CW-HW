numbers = [3,3,4,6,8,35,76];

const sum = numbers.reduce((arr, cur) => {
    return arr + cur
})

console.log(sum)