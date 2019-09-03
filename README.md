My personal website! This project represents my first experience coding in
HTML and CSS. I am using my own Google domain and plan on updating the site
as I work on more projects that I will be adding to my portfolio.

### UPDATES

I am very proud of a few recent features I have added to this site:
1. the timeline page of my academic journey till now (check it out! suggestion: best enjoyed on full-screen on a computer but mobile-friendly)
2. I wrote some Javascript so that the header image of both html pages changes depending on the day of the month

Here is the code for that:
```Javascript
<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
<script>
$(document).ready(function(){
	var header = $('body');
	var d = new Date();
	var n = d.getDate();
	var str1 = 'url("images/banner';
	var str2 = '.JPG")';
	var background = str1.concat(n, str2);
	var current = 0;
	header.css('background-image', background);
	header.css('background-size', 'cover');
});
</script>
```


### CREDITS

* Spectral by HTML5 UP
* Unsplash (unsplash.com)
* Font Awesome (fontawesome.io)
* jQuery (jquery.com)
* Scrollex (github.com/ajlkn/jquery.scrollex)
* Responsive Tools (github.com/ajlkn/responsive-tools)
* HELP --> w3 (https://www.w3schools.com/)
