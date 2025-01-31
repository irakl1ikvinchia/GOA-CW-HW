// კლასის შექმნა და ინიციალიზაცია**: შექმენი კლასი `User`, რომელსაც ექნება თვისებები 
// `name` და `email`. კონსტრუქტორის მეშვეობით ინიციალიზაცია გაუკეთე ამ თვისებებს და შექმენი რამდენიმე `User` ობიექტი.


class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }
    
    printinfo(){
        console.log(`name: ${name}`, `email: ${email}`)
    }
}

const user1 = new User(this.name, this.email);

console.log(user1);