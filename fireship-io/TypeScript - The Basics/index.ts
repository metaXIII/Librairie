import * as _ from "lodash"

async function hello() {
    return "aze"
}

let lucky: any = 23

const url = new URL("...")

lucky = "23"

type Style = "bold" | "italic"

let font: Style //can only be bold or italic

interface Person {
    first: string,
    last: string,
    [key: string]:any
}

const person: Person = {
    first: "aze",
    last: "aze2"
}

const other: Person = {
    first: "!aze",
    last: "!aze2",
    fast: true
}

const array: number[] = []

array.push(1)

type Mylist = [number?, string?, boolean?]
const arr = []

arr.push(1)
arr.push('1')
arr.push(true)

class Observable<T> {
    constructor(public value: T) {

    } 
}

let x: Observable<number>
let y: Observable<Person>
let z = new Observable(25)