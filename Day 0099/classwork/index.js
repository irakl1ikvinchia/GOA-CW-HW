class Human {
    constructor(name, lastName) {
        this.name = name;
        this.lastName = lastName;
    }
    
    printInfo() {
        console.log(this.name, this.lastName)
    }
}

class Worker extends Human {
    constructor(name, lastName, position) {
        super(name, lastName);
        this.position = position;
    }
}

const worker1 = new Worker("irakli", "kvinchia", "miniMosw");
worker1.printInfo()

console.log(worker1)