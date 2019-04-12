 ////////////////////////////////////////////////////////////////////////////////////////////////
 // Web Assignment2
 // group:
 // Kevin christopher 815007355
 ////////////////////////////////////////////////////////////////////////////////////////////////


 var Genres = [];
 var animes = [];
 document.getElementById("addAnime").addEventListener("submit", formEntry);
 //  document.addEventListener("DOMContentLoaded", loadGenres);
 //  document.addEventListener("DOMContentLoaded", loadMovies);
 $(document).ready(function () {
     $('[data-tooltip="tooltip"]').tooltip();
 });

 function formEntry() {


     var id = document.getElementById("Anime_ID").value.toLowerCase();
     var nam = document.getElementById("Name").value.toLowerCase();
     var type = document.getElementById("type").value.toLowerCase();
     var epiNo = document.getElementById("epi").value.toLowerCase();
     var rating = document.getElementById("rating").value.toLowerCase();
     addGenre();
     var Members = document.getElementById("members").value.toString().toLowerCase();
     if (isValidID(animes, id)) {
         var anime = createAnime(id, nam, Genres, type, epiNo, rating, Members);
         animes.push(anime);
         displayMovies();
         clearForm();
         displayGenre();

     }
     console.log(Genres);
     console.log(animes);


 }

 function clearForm() {
     document.getElementById("Anime_ID").value = "";
     document.getElementById("Name").value = "";
     document.getElementById("type").value = "";
     document.getElementById("epi").value = "";
     document.getElementById("rating").value = "";
     document.getElementById("members").value = "";
     Genres.splice(0, Genres.length);

 }

 function isValidID(arr, id) {
     if (id > 0) {
         for (var i in animes) {
             if (arr[i].Anime_ID === id) {
                 alert("id must be unique");
                 return false;
             }
         }
         return true;
     }

     console.log(id);
     console.log(nam);
     console.log(Genres);
     console.log(type);
     console.log(epiNo);
     console.log(rating);
     console.log(Members);
     return false;
 }

 function addGenre() {
     var newRecord = document.getElementById("genre").value.toString().toLowerCase();

     for (var i in Genres) {
         if (Genres[i] === newRecord) {
             return true;
         }
     }

     addToArr(Genres, newRecord);

     document.getElementById("genre").value = "";
     displayGenre();
     return true;

 }

 function addToArr(array, newRecord) {
     if (newRecord !== "" && newRecord !== undefined) {
         if (array.length === 0) {
             array.push(newRecord);
             return true;
         } else
             for (var i = 0; i < array.length; i++) {
                 if (newRecord.toLowerCase() < array[i].toLowerCase()) {
                     array.splice(i, 0, newRecord);
                     return true;
                 }
             }
         array.push(newRecord);


         return true;
     }
     return false;

 }








 function displayGenre() {
     var str = '<ul>';
     for (var i in Genres) {
         str += '<li>' + Genres[i] + '</li>';
     }
     str += '</ul>';
     document.getElementById('genreList').innerHTML = str;
 }

 function createAnime(id, nam, gen, type, epiNo, rating, mem) {
     var A = new Anime();
     A.Anime_ID = id;
     A.Name = nam;
     for (var i in gen) {
         A.genre[i] = gen[i];
     }
     A.type = type;
     A.epi = epiNo;
     A.rating = rating;
     A.members = mem;

     return A;
 }
 /////////////////////////////////////////////////////////////////////