$(document).ready(function () {
    // handle product hover effect
    const product = $('.product');
    const advantage = $('.advantage');

    product.mouseenter(function () {
        TweenMax.to(this, 0.3, {y: -10, boxShadow: '0 5px 10px rgba(0, 0, 0, 0.27), 0 0 40px rgba(0, 0, 0, 0.06) inset'});
    });
    product.mouseleave(function () {
        TweenMax.to(this, 0.3, {y: 0, boxShadow: '0 1px 4px rgba(0, 0, 0, 0.27), 0 0 40px rgba(0, 0, 0, 0.06) inset'})
    });

    advantage.mouseover(function () {
        TweenMax.to(this, 0.3, {y: -10, boxShadow: '0 5px 10px rgba(0, 0, 0, 0.27), 0 0 40px rgba(0, 0, 0, 0.06) inset'})
    });
    advantage.mouseout(function () {
        TweenMax.to(this, 0.3, {y: 0, boxShadow: '0 1px 4px rgba(0, 0, 0, 0.27), 0 0 40px rgba(0, 0, 0, 0.06) inset'})
    });


});