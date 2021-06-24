// L1
console.log("🥪 Synchronous 1")

// L2
setTimeout(() => console.log("🍎 time out 2"), 0)

// L3
Promise.resolve().then(() => {
    console.log("🍍 Promise 3")
})

// L4
console.log("🥪 Synchronous 4")

//1, 4, 3, 2