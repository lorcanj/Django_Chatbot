function hello() {
    document.querySelector("#test").innerHTML = "I have changed the text of this";
}

let counter = 0;

function count() {
    counter++;
    document.querySelector('#number').innerHTML = counter;

    if (counter % 10 === 0) {
        alert('Count is now ${counter}');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = hello;
});