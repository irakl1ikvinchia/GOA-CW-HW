// .push() ამატებს სიის ბოლოში ელემენტს;
// .pop() შლის სიის ბოლო ელემენტს;
// .shift() შლის სიის პირველ ელემენტს;
// .unshift() ამატებს სიის დასაწყისში ელემენტს;
// .slice() გადაეცემა 3 მნიშვნელობა start, end და step, აბრუნებს ახალ სიას;
// .splice() გადაეცამა ორი მნიშვნელობა index და რაოდენობა;


const carList = ["BMW", "TOYOTA", "MERSEDES", "AUDI", "PORSCHE", "FORD"]

carList.push("alfaRomeo")
carList.pop()
carList.shift()
carList.unshift("BMW")
carList.splice(1, 2)

console.log(carList)