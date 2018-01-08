# HTML jinja2 template for Google Book search task

__author__ = 'Tanya and Isabel'

#write your HTML template in the variable below
gBooksTemplate = """
<html>
<head>
  <meta charset="UTF-8">
  <title>Google Books Search</title>
  <link href='http://fonts.googleapis.com/css?family=Economica:400,700' rel='stylesheet'>
  <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Searching Google Books</h1>
    <p>Your search query <strong>"{{query1}}"</strong> has a total of "{{totalCount}}":</p>
    <p>Below are the first "{{displayCount}}" returned items.</p>

<div id="main">
{% for books in booksList %}
<div class="book">
   <h3>{{books['title']}} - {{books['author']}}</h3>
   <img src="{{books['imgURL']}}"><br>
   <p>Publication Year: {{books["publishedDate"]}}.  Page count: {{books["pageCount"]}}</p>
   <p>{{books["description"]}}</p>
   <a href="{{books['previewLink']}}">Visit preview page</a>
</div>
{% endfor %}
</div>
</body>
</html>
"""
