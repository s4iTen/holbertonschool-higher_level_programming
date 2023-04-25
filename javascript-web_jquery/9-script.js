#!/usr/bin/node
$(document).ready(function () {
  $.ajax({
    url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
    dataType: 'jsonp',
    success: function (data) {
      const helloTranslation = data.hello;
      $('#hello').text(helloTranslation);
    }
  });
});
