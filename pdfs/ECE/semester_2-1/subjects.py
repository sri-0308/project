subjects = [
    {"name": "BEEE – Basic Electrical and Electronics Engineering", "units": [1, 2, 3, 4, 5]},
    {"name": "LAC – Linear Algebra and Calculus", "units": [1, 2, 3, 4, 5]},
    {"name": "Drawing – Engineering Drawing", "units": [1, 2, 3, 4, 5]},
    {"name": "Physics – Engineering Physics", "units": [1, 2, 3, 4, 5]},
    {"name": "C Language – C Programming Language", "units": [1, 2, 3, 4, 5]}
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{subject_name} Materials</title>
    <style>
        body {{
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #1E3C72, #2A5298);
            color: #fff;
            text-align: center;
            padding: 20px;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.5);
        }}
        .pdf-list {{
            list-style: none;
            padding: 0;
        }}
        .pdf-list li {{
            margin: 10px 0;
        }}
        .pdf-list a {{
            text-decoration: none;
            color: #FFD700;
            font-weight: bold;
        }}
        .pdf-list a:hover {{
            text-decoration: underline;
            color: #FFC107;
        }}
    </style>
</head>
<body>
    <h1>📘 {subject_name} Materials</h1>
    <div class="container">
        <ul class="pdf-list">
            {unit_links}
        </ul>
    </div>
</body>
</html>"""

unit_link_template = '<li><a href="unit{unit}.pdf" target="_blank" download>Unit {unit}</a></li>'

for subject in subjects:
    unit_links = "".join([unit_link_template.format(unit=unit) for unit in subject["units"]])
    html_content = html_template.format(subject_name=subject["name"], unit_links=unit_links)

    # Saving HTML files for each subject with UTF-8 encoding
    with open(f"{subject['name'].replace(' ', '_').replace('–', '_')}_Materials.html", "w", encoding="utf-8") as file:
        file.write(html_content)

print("HTML files generated for all subjects.")
