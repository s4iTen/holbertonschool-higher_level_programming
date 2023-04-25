#!/usr/bin/node
$(document).ready(function () {
  const header = $('header');
  $('DIV#red_header').click(function () {
    header.classlist.add('red');
  });
});
