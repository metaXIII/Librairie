import { Observable, of, from, fromEvent, interval, asyncScheduler} from 'rxjs'

export const print = (v) => {
    const el = document.createElement('h3');
    el.innerText = '🔵 ' + v;
    document.body.appendChild(el);
}


// const basic  = Observable.create(observer => {
//     observer.next('A')
//     observer.next('B')
//     observer.complete();
//     observer.next('C') //non affiché
// })

// basic.subscribe(print)

// const hello = of('hello')
// hello.subscribe(print)


// const world = from('world');
// world.subscribe(print)

// const event = fromEvent(document, 'click')
// event.subscribe(print)

// const perdiodic = interval(500)
// perdiodic.subscribe(print)

const hello = of('hello', asyncScheduler)
hello.subscribe(print)
print('world')