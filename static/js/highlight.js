$( document ).ready(
    function() {
        let highlightClassName = "anchor-aid-highlight";
        let anchors = document.getElementsByTagName('a');
        for (let i = 0; i < anchors.length; i++)
            anchors[i].target = '_blank';
        let $text = $('*:contains("' + parent.search.name + '"):last');
        $text.highlight(parent.search.name, highlightClassName);
        $("." + highlightClassName).css('background-color', 'yellow');
        $('html, body').animate({
            scrollTop: $text.offset().top * .93,
            scrollLeft: $text.offset().left
        });

    }
);

jQuery.fn.highlight = function (str, className) {
    let regex = new RegExp(str, "gi");
    return this.each(function () {
        $(this).contents().filter(function() {
            return this.nodeType === 3 && regex.test(this.nodeValue);
        }).replaceWith(function() {
            return (this.nodeValue || "").replace(regex, function(match) {
                return "<span class=\"" + className + "\">" + match + "</span>";
            });
        });
    });
};