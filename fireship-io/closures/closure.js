for (var i = 0; i < 3; i ++) {

    const log = () => {
        console.log(i)
    }
    setTimeout(log, 100)
} //3,3,3


for (let i = 0; i < 3; i ++) {

    const log = () => {
        console.log(i)
    }
    setTimeout(log, 100) //1,2,3
}