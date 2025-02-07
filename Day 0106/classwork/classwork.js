const promise = new promise((resolve, reject) => {
    const book = True;
    
    if (book) {
        resolve("Task completed successfully");
    } else {
        reject("Task failed")
    }
});

book
    .then((result) => console.log("fullfiled:", resolve))
    .cath((eror) => console.log("eror:", reject))