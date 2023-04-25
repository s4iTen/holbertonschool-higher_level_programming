#!usr/bin/node
$(document).ready(function () {
  $('#character').click(function () {
    $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
      const characterName = data.name;
      $('#character').text(characterName);
    });
  });
});
