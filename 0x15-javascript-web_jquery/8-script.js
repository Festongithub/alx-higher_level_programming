// fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  console.log(data);
  data.result.forEach(film => {
    $('UL#list_movies').append(film.title);
  });
});
