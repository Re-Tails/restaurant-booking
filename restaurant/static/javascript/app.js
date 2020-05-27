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
  showMain();
  hideEntree();
  hideDessert();
}

function displayDessert(){
  showDessert();
  hideEntree();
  hideMain();
}

function displayAll(){
  showEntree();
  showMain();
  showDessert();
}

function showEntree(){
  var entree = document.getElementById("entreeDIV");
  if(entree.style.display === "none"){
    entree.style.display = "block";
  }
}

function showMain(){
  var main = document.getElementById("mainDIV");
  if(main.style.display === "none"){
    main.style.display = "block";
  }
}

function showDessert(){
  var dessert = document.getElementById("dessertDIV");
  if(dessert.style.display === "none"){
    dessert.style.display = "block";
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
