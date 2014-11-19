var homeHash = '#home';

// smooth scrolling
$("a[href*='#']").on('click', function (e) {

    if (this.href.split('#')[0] == window.location.href.split('#')[0]) {

        // prevent default anchor click behavior
        e.preventDefault();

        // store hash
        var hash = this.hash;

        // animate
        $('.parallax').animate({
            scrollTop: $(this.hash).offset().top - $('.parallax :first-child').offset().top
        }, 500, function () {

            if (hash == homeHash) {
                removeHash();
            } else {
                // when done, add hash to url
                // (default click behaviour)
                // TODO: disabling because parallax backgrounds get weird when jumping to colleges
                //window.location.hash = hash;
            }
        });
    }
});