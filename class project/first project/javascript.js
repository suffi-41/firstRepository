
const login = document.getElementById('#login_button');
let layout_display = document.querySelector('.layout');
layout_display.style.display = 'none';

function background_color(value, seccond_value){
      document.body.style.background=value;
      
}
function color(value){
    document.body.style.color=value;
}

function login_function(value) {
    let login = value;
    let login_page = document.querySelector('.login_page');
    let ragistration_page = document.querySelector('.ragistration_page');
    let display = document.querySelector('.layout');

    if (value == "logout") {
        display.style.display = "none";
        
    }

    else if (value == 'ragistration') {
        display.style.display = '';
        ragistration_page.classList.add("transform");
        login_page.classList.add("animation");
    }
    else{
         display.style.display = '';
         login_page.classList.add("transform");

    }
}

let profile = document.querySelector("#profile");
profile.addEventListener('click', alert('hello'));


console.log("hello")

// let my_joke=[
//     {
//         "category": "Programming",
//         "type": "single",
//         "joke": "I've got a really good UDP joke to tell you but I don’t know if you'll get it.",
//         "flags": {
//             "nsfw": false,
//             "religious": false,
//             "political": false,
//             "racist": false,
//             "sexist": false,
//             "explicit": false
//         },
//         "id": 0,
//         "safe": true,
//         "lang": "en"
//     },
//     {
//         "category": "Programming",
//         "type": "single",
//         "joke": "Java and C were telling jokes. It was C's turn, so he writes something on the wall, points to it and says \"Do you get the reference?\" But Java didn't.",
//         "flags": {
//             "nsfw": false,
//             "religious": false,
//             "political": false,
//             "racist": false,
//             "sexist": false,
//             "explicit": false
//         },
//         "id": 4,
//         "safe": true,
//         "lang": "en"
//     }
// ]

// let index=Math.floor(Math.random()*my_joke.length-1)
// let joke = document.getElementById('joke');
// joke.innerHTML= my_joke[index].joke;
