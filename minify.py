import re, os

cwd = os.getcwd()
path = os.path.join(cwd, "index.html")
html = open(path, "r", encoding="utf-8").read()

orig_size = len(html)

# ====== 1. HTML minification ======
# Strip leading whitespace from each line
lines = []
for line in html.split("\n"):
    stripped = line.strip()
    if stripped:
        lines.append(stripped)
html = "\n".join(lines)

# ====== 2. CSS minification (inside <style>...</style>) ======
def minify_css(css):
    css = re.sub(r"\s*{\s*", "{", css)
    css = re.sub(r"\s*}\s*", "}", css)
    css = re.sub(r"\s*:\s*", ":", css)
    css = re.sub(r"\s*;\s*", ";", css)
    css = re.sub(r"\s*,\s*", ",", css)
    css = re.sub(r";}", "}", css)  # Remove last semicolon before }
    return css

style_match = re.search(r"<style>(.*?)</style>", html, re.DOTALL)
if style_match:
    minified_css = minify_css(style_match.group(1))
    html = html[:style_match.start(1)] + minified_css + html[style_match.end(1):]

# ====== 3. Basic JS minification (safe whitespace removal) ======
def minify_js(js):
    # Remove single-line comments
    js = re.sub(r"//[^\n]*\n", "\n", js)
    # Safe whitespace removal
    js = re.sub(r"\s*=\s*", "=", js)
    js = re.sub(r"\s*\+\s*", "+", js)
    js = re.sub(r"\s*\{\s*", "{", js)
    js = re.sub(r"\s*\}\s*", "}", js)
    js = re.sub(r"\s*\(\s*", "(", js)
    js = re.sub(r"\s*\)\s*", ")", js)
    js = re.sub(r"\s*;\s*", ";", js)
    js = re.sub(r"\s*,\s*", ",", js)
    js = re.sub(r"\s*===\s*", "===", js)
    js = re.sub(r"\s*!==\s*", "!==", js)
    js = re.sub(r"\s*\+\+", "++", js)
    js = re.sub(r"\s*&&\s*", "&&", js)
    js = re.sub(r"\s*\|\|\s*", "||", js)
    # Remove extra semicolons
    js = re.sub(r";;+", ";", js)
    # Trim
    js = js.strip()
    return js

script_match = re.search(r"<script>(.*?)</script>", html, re.DOTALL)
if script_match:
    minified_js = minify_js(script_match.group(1))
    html = html[:script_match.start(1)] + minified_js + html[script_match.end(1):]

# ====== 4. Remove any remaining double blank lines ======
html = re.sub(r"\n{3,}", "\n\n", html)

open(path, "w", encoding="utf-8").write(html)
saved = orig_size - len(html)
pct = (saved / orig_size) * 100
print(f"Before: {orig_size} bytes")
print(f"After:  {len(html)} bytes")
print(f"Saved:  {saved} bytes ({pct:.1f}%)")
