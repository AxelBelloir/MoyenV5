const DIV_principal = ["overlay","DIV_home","DIV_login","DIV_average","DIV_chess"];
let dataSend = "login";

function reinsertionText(){ // Remet les B=bons textes dans les titres, les paragraphes et les variables
  document.getElementById("H2_login").textContent = "Login";
  dataSend = "login";
}


function openDIV(DIV){ // Ferme les ancienne div et ouvre la nouvelle
  if(DIV != "DIV_login"){ 
    for(let i = 0; i < DIV_principal.length;++i){
      document.getElementById(DIV_principal[i]).style.display =  "none";
    }
  } else { document.getElementById("overlay").style.display = "block";}
  reinsertionText();
  document.getElementById(DIV).style.display = "block";
}

function createPage(){ // Change la page de Login vers Create (sans dupliquer en html)
  dataSend = "create";
  document.getElementById("H2_login").textContent = "Create";
}
