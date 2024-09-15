$(document).ready(function() {
    setTimeout(function() {
        $(".msgs").fadeTo(500, 0).slideUp(500, function() {
            $(this).remove();
        });
    }, 1000);
});