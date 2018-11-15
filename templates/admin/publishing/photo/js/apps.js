function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('.field-photo').attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

$('.field-photo', $('input')).change(function(){
    readURL(this);
});

