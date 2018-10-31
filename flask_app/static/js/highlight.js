$( document ).ready(
    function() {
        let anchors = document.getElementsByTagName('a');
        for (let i = 0; i < anchors.length; i++)
            anchors[i].target = '_blank';
        let $text = $('*:contains("' + parent.search + '"):last');
        $text.css('background-color', 'yellow');
        $('html, body').animate({
            scrollTop: $text.offset().top,
            scrollLeft: $text.offset().left
        });
    }
);