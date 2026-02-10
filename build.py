import os
import markdown

TEMPLATE_TOP = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="../style.css">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono&display=swap" rel="stylesheet">
</head>
<body>
<header class="banner"></header>
<nav class="nav">
<a href="../index.html">Home</a>
<a href="../blog.html" class="active">Blog</a>
</nav>
<main>
"""

TEMPLATE_BOTTOM = """
</main>
</body>
</html>
"""

posts = []

for file in sorted(os.listdir("posts"), reverse=True):
    if file.endswith(".md"):
        path = os.path.join("posts", file)
        with open(path) as f:
            lines = f.readlines()

        title = lines[0].replace("Title: ", "").strip()
        date = lines[1].replace("Date: ", "").strip()
        content = "".join(lines[3:])

        html_content = markdown.markdown(content)

        out_file = file.replace(".md", ".html")
        with open(os.path.join("posts", out_file), "w") as out:
            out.write(TEMPLATE_TOP)
            out.write(f"<h1>{title}</h1><p>{date}</p>")
            out.write(html_content)
            out.write(TEMPLATE_BOTTOM)

        posts.append(f'<div class="project"><h3><a href="posts/{out_file}">{title}</a></h3><p>{date}</p></div>')

with open("blog.html", "w") as blog:
    blog.write(TEMPLATE_TOP)
    blog.write("<h1>Blog</h1>")
    for p in posts:
        blog.write(p)
    blog.write(TEMPLATE_BOTTOM)
