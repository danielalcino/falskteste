$(document).ready(function(){
    $('input[type="tel"]').mask('900 000 000');

    // Aplica classe "filled" nos inputs com valor inicial
    $('input').each(function() {
        if ($(this).val()) {
            $(this).addClass('filled');
        }
    });

    // Ao digitar ou sair do campo
    $('input').on('input blur', function() {
        if ($(this).val()) {
            $(this).addClass('filled');
        } else {
            $(this).removeClass('filled');
        }
    });
});