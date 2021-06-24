import fetch from 'node-fetch'

const promise = fetch('https://jsonplaceholder.typicode.com/todos/1');

promise
    .then((res) => res.json())
    .then(user => {
        console.log("😊", user.title)
        throw new Error("uh oh")
    })
    .catch(err => console.error("😭", err))

console.log("🥪 synchronous")