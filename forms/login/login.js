document.getElementById("sitio-web-asiste").addEventListener("click", function(){
  window.location.href="https://github.com/AND3SIL4/Proyecto-ASISTE"
});
document.getElementById("sitio-web-sena").addEventListener("click", function(){
  window.location.href="https://sena.territorio.la/cms/index.php"
});
document.getElementById("registro-usuarios").addEventListener("click", function(){
  // alert("Regristro de usuarios...")
  window.location.href="../registrer/aprendices/registre.html"
})

document.getElementById('inicio-sesion').addEventListener('click', function(event){
  event.preventDefault();

  let userDocument = document.getElementById('user-document').value;
  let userName = document.getElementById('user-name').value;
  let userPassword = document.getElementById('user-password').value;

  if(userDocument === 'CC' && userName === 'andres' && userPassword === '12345'){
    console.log('Inicio de sesion exitoso...');
    // SweetAlert 
    Swal.fire({
      title: 'Successful..!',
      icon: 'success',
      showCancelButton: false,
      showConfirmButton: true,
      timer: 3000
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href="https://github.com/AND3SIL4/Proyecto-ASISTE"
      }
    })
    
  }else{
    // alert('Credenciales invalidas')
    // document.getElementById('error-message').textContent = 'Datos incorrectos';
    console.log('Datos incorrectos...');
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: 'Datos incorrectos...',
      showConfirmButton: false,
      timer: 1000
    })
  }
});


