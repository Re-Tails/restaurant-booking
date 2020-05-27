alert("test");

// function showEntree(){
//   var x = document.getElementById("entreeDiv");
//   if (x.style.display === "none"){
//     x.style.display = "block";
//   } else {
//     x.style.display = "none";
//   }
// }

function displayEntree(){
  showEntree();
  hideMain();
  hideDessert();
}

function displayMain(){

}

function displayDessert(){
  
}

function showEntree(){
  var entree = document.getElementById("entreeDIV");
  if(entree.style.display === "none"){
    entree.style.display = "block";
  }
}

function hideEntree(){
  var entree = document.getElementById("entreeDIV");
  entree.style.display = "none";
}

function hideMain(){
  var main = document.getElementById("mainDIV");
  main.style.display = "none";
}

function hideDessert(){
  var dessert = document.getElementById("dessertDIV");
  dessert.style.display = "none";
}
