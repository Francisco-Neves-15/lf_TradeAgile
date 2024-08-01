function adjustIframeHeight(iframe) {
    // Define a altura do iframe para o conteúdo interno
    iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
}