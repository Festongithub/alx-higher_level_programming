//  fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello

const $ = window.$;
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, status) {
  console.log(data.hello);
  $('#hello').html(data.hello);
});
