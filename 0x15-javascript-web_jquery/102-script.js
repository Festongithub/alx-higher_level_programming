// script that fetches and prints how to say “Hello” depending on the language
// from the api https://www.fourtonfish.com/hellosalut/hello/

const $ = window.$;
$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
