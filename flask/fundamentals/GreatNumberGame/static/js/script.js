function validateForm() {
    var x = document.forms["guess"]["guess"].value;
    if (x == "") {
        alert("Make a guess!");
        return false;
    }
}