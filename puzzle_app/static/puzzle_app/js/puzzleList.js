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

function appear() {
    document.querySelector('#test').style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#test').style.display = 'none';
    document.querySelector('#increase').onclick = hello;
    document.querySelector('#disappear').onclick = appear;
});