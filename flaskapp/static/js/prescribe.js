 // Example starter JavaScript for disabling form submissions if there are invalid fields
 (function () {
    'use strict';
    window.addEventListener('load', function () {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');

                
                if(form.checkValidity() === true){
                    //enter your code here 
                    event.preventDefault();
                     var form_data = {
                         name : name_id.value,
                         username : username_id.value,
                         password : password_id.value
                     }  

                     console.log(form_data); //printing form data in Console
                     document.forms[0].reset();    //reseting the form
                     document.getElementById('myForm').classList.remove("was-validated");//reseting the form validation

                }

            }, false);
        });
    }, false);
})();

// $(document).ready(function(){
//     $(window.location.hash).modal('show');
//     $('a[data-toggle="modal"]').click(function(){
//        window.location.hash = $(this).attr('href');
//     });
//  });