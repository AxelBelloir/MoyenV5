const DIV_principal = ["overlay","DIV_home","DIV_login","DIV_average","DIV_chess"];
let dataSend = "login";





function createPage(){ // Change la page de Login vers Create et inversement (sans dupliquer en html)
  const elmentTOcreate = ["create", "create", "back login", "create"];
  const elmentTOlogin = ["login", "login", "create", "login"];
  let elment;
  if(dataSend == "login"){elment = elmentTOcreate;} else {elment = elmentTOlogin;}
  dataSend = elment[0];
  document.getElementById("H2_login").textContent = elment[1];
  document.getElementById("BUT_login1").textContent = elment[2];
  document.getElementById("BUT_login2").textContent = elment[3];
}
function reinsertionText(){
  dataSend = "login";
  document.getElementById("H2_login").textContent = "login";
  document.getElementById("BUT_login1").textContent = "create";
  document.getElementById("BUT_login2").textContent = "login";
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
