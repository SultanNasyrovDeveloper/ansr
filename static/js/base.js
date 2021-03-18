$(document).ready(function () {
    $(".phone-input").mask("+7(999) 999-99-99");

    function closeAlert () {
        let alert = $('.alert-msg-container');
        TweenMax.to(alert, 0.3, {opacity: 0, display: 'none'})

    };

    setTimeout(closeAlert, 4000);
});