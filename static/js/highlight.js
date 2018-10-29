$( document ).ready(
    function() {
        var urlParams = new URLSearchParams(window.location.search);
        var searchText = urlParams.get('search');
        var $text = $('*:contains("' + searchText + '"):last')
        $text.css('background-color', 'yellow');
        $('html, body').animate({
            scrollTop: $text.offset().top,
            scrollLeft: $text.offset().left
        });
    }
)