let getData = function (data) {
    if (data && data.contents && data.status.http_code === 200) loadHTML(data.contents);
    else loadHTML('Error: Cannot load ' + url);
};

let loadURL = function (src) {
    url = src;
    let script = document.createElement('script');
    script.src = 'https://allorigins.me/get?url=' + encodeURIComponent(url) +'&callback=getData';
    document.body.appendChild(script);
};

let loadHTML = function (html) {
    let jQ = '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>';
    let highlight = '<script src="./static/js/highlight.js"></script>';

    let iframe = document.getElementById('site');
    iframe.src = 'about:blank';
    var urlObj =  new URL(site);
    html.replace(/<head>/i, '<head>' + jQ + highlight + '<base target="_blank" href="' + url + '"><scr' + 'ipt>document.addEventListener("click", function(e) { if(e.target && e.target.nodeName == "A") { e.preventDefault(); parent.loadURL(e.target.href); } });</scr' + 'ipt>');
    var newHTML = replace_all_rel_by_abs(urlObj, html);
    iframe.contentWindow.document.open();
    iframe.contentWindow.document.write(newHTML);
    iframe.contentWindow.document.close();
};

let initializeCopyTooltip = function () {
    $("#current-link").text(window.location.href);
    $("#current-link").href = window.location.href;
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

