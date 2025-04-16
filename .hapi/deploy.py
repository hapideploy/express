from hapi.cli import app
from hapi.recipe import Express

app.load(Express)

app.put("name", "express")
app.put("repository", "https://github.com/hapideploy/express")
app.put("branch", "main")

app.add("shared_dirs", [])
app.add("shared_files", [])
app.add("writable_dirs", [])
