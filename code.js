function submitbtn() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;
    //console.log(name.value+" "+email.value+" "+message.value);
    if(name == ''){
        alert("name cannot be empty");
    }
    if(email == ''){
        alert("email cannot be empty")
    }
    if(message == ''){
           alert("message cannot be empty"); 
    }
    alert(name.length)

    var mytime = setTimeout(mytimeout(),1000);
    function mytimeout(){
        var temp = '<p>hello world</p>';
        document.getElementsByClassName('container')[0].innerHTML += temp;
    }
};




