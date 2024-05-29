$(document).ready(function() {
	$('#btn_translate').click(function() {
		const lan = $('#language_code').val();
                const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lan;
                $.getJSON(apiUrl, function(data) {
                    $('#hello').text(data.hello);
		});
        });
});
