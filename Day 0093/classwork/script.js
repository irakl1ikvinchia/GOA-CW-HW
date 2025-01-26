//  N1

const names = ["me", "var", "erti", "cida", "me", "sicili", "minda", "DD"];

const firstMethod = names.forEach((curName, index, arr) => {
    console.log(`curvalue: ${curName}, index: ${index}`)
})


// N2

const namess = ["me", "var", "erti", "cida", "me", "sicili", "minda", "DD"];

const secondMethod = namess.map((curName, index, arr) => {
    console.log(curName + index);
})