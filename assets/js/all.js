$(document).ready(function () {
    var $subscribeForm = $("form[id='subscribeForm']");

    $subscribeForm.validate({
        rules: {
            contact_email: {
                required: true,
                email: true
            }
        },
        messages: {
            email: "Please enter a valid email address"
        },
        errorElement: "em",
        errorPlacement: function (error, element) {
            // Add the `help-block` class to the error element
            error.addClass("help-block");

            if (element.prop("type") === "checkbox") {
                error.insertAfter(element.parent("label"));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function (element, errorClass, validClass) {
            $(element).parents(".form-group").addClass("has-error").removeClass("has-success");
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).parents(".form-group").addClass("has-success").removeClass("has-error");
        }
    });

});


