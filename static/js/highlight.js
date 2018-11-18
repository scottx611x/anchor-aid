$( document ).ready(
    function() {
        jQuery.fn.highlight = function (str, className) {
            let regex = new RegExp(str, "gi");
            return this.each(function () {
                $(this).contents().filter(function() {
                    return (this.nodeType === 3 || this.nodeType === 9) && regex.test(this.nodeValue);
                }).replaceWith(function() {
                    return (this.nodeValue || "").replace(regex, function(match) {
                        return "<span class=\"" + className + "\">" + match + "</span>";
                    });
                });
            });
        };

        let highlightClassName = "anchor-aid-highlight";
        let $text = $('*:contains("' + parent.search.name + '"):last');
        $text.highlight(parent.search.name, highlightClassName);
        $("." + highlightClassName).css('background-color', 'yellow');
        $('html, body').animate({
            scrollTop: $text.offset().top * .975,
            scrollLeft: $text.offset().left
        });

    }
);
