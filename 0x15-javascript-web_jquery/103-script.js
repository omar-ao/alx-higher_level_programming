$(document).ready(() => {
  const btn = $('#btn_translate');
  const hello = $('#hello');
  const lang = $('#language_code');

  btn.click(fetchData);

  btn.keypress(function (event) {
    if (event.keyCode === 13) {
      fetchData();
    }
  });

  function fetchData () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang.val().trim();
    $.ajax({
      type: 'GET',
      dataType: 'json',
      url: url,
      success: function (data) {
        hello.html('<span>' + data.hello + '</span>');
      }
    });
  }
});
