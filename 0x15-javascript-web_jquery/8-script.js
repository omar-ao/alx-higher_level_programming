$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(films) {
	$.each(films.results, function(i, film) {
		$('#list_movies').append($('<li>').text(film.title));
	}); 
});
