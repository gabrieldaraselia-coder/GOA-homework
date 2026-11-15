const body = document.body

const nameHeading = document.createElement("h1");
nameHeading.innerText = "John Doe";
body.appendChild(nameHeading);


const bioPara1 = document.createElement("p");
bioPara1.innerText = "Hello! My name is John Doe.\nI am learning web development and this is my very first HTML page.";
body.appendChild(bioPara1);


const hr1 = document.createElement("hr");
body.appendChild(hr1);


const bioPara2 = document.createElement("p");
bioPara2.innerText = "I love coding and exploring new technologies.";
body.appendChild(bioPara2);


const hr2 = document.createElement("hr");
body.appendChild(hr2);


const booksHeading = document.createElement("h2");
booksHeading.innerText = "My Favorite Books";
body.appendChild(booksHeading);


const ul = document.createElement("ul");

const book1 = document.createElement("li");
book1.innerText = "Harry Potter";
ul.appendChild(book1);

const book2 = document.createElement("li");
book2.innerText = "The Hobbit";
ul.appendChild(book2);

const book3 = document.createElement("li");
book3.innerText = "Atomic Habits";
ul.appendChild(book3);

body.appendChild(ul);



const moviesHeading = document.createElement("h2");
moviesHeading.innerText = "My Favorite Movies";
body.appendChild(moviesHeading);


const ol = document.createElement("ol");

const movie1 = document.createElement("li");
movie1.innerText = "Inception";
ol.appendChild(movie1);

const movie2 = document.createElement("li");
movie2.innerText = "Interstellar";
ol.appendChild(movie2);

const movie3 = document.createElement("li");
movie3.innerText = "Avengers: Endgame";
ol.appendChild(movie3);

body.appendChild(ol);