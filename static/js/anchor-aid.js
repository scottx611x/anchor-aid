/*
Based off of: "Bypassing X-Frame-Options in <iframe> using YQL"
See https://stackoverflow.com/a/25587469
*/

let getData = function (data) {
    if (data && data.query && data.query.results && data.query.results.resources && data.query.results.resources.content && data.query.results.resources.status == 200) loadHTML(data.query.results.resources.content);
    else if (data && data.error && data.error.description) loadHTML(data.error.description);
    else loadHTML('Error: Cannot load ' + url);
};

let loadURL = function (src) {
    url = src;
    let script = document.createElement('script');
    script.src = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20data.headers%20where%20url%3D%22' + encodeURIComponent(url) + '%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=getData';
    document.body.appendChild(script);
};

let loadHTML = function (html) {
    let jQ = '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>';
    let highlight = '<script src="./static/js/highlight.js"></script>';

    let iframe = document.getElementById('site');
    iframe.src = 'about:blank';
    iframe.contentWindow.document.open();
    iframe.contentWindow.document.write(html.replace(/<head>/i, '<head>' + jQ + highlight + '<base target="_blank" href="' + url + '"><scr' + 'ipt>document.addEventListener("click", function(e) { if(e.target && e.target.nodeName == "A") { e.preventDefault(); parent.loadURL(e.target.href); } });</scr' + 'ipt>'));
    iframe.contentWindow.document.close();
};

let initializeCopyTooltip = function () {
    $("#current-link").text(window.location.href);
    $("#copy-link-button").tooltip({
      trigger: 'click',
      placement: 'bottom'
    });

    function setTooltip(message) {
      $("#copy-link-button").tooltip('hide')
        .attr('data-original-title', message)
        .tooltip('show');
    }

    function hideTooltip() {
      setTimeout(function() {
        $("#copy-link-button").tooltip('hide');
      }, 1000);
    }

    // Clipboard

    var clipboard = new ClipboardJS("#copy-link-button");

    clipboard.on('success', function(e) {
      setTooltip('Copied!');
      hideTooltip();
    });

    clipboard.on('error', function(e) {
      setTooltip('Failed!');
      hideTooltip();
    });
};

window.onload = function() {
    let iframe = document.getElementById('site');
    loadURL(site);
    initializeCopyTooltip();
};

