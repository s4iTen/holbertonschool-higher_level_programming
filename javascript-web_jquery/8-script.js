#!/usr/bin/node
$(document).ready(function () {
  $('#list_movies').click(function () {
    $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
      const movies = data.results;
      let movieList = '';

      for (let i = 0; i < movies.length; i++) {
        movieList += '<li>' + movies[i].title + '</li>';
      }

      $('#list_movies').html('<ul>' + movieList + '</ul>');
    });
  });
});
