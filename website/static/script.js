function reloadPage() {
  window.location.reload();
}

function alertUser() {
  if (tokenTest != "") {
    alert("You have already logged in!");
    window.location.replace("/");
  }
}
