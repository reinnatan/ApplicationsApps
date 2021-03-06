import os

from flask_script import Manager, Server
from application import create_app
app = create_app()
manager = Manager(app)

manager.add_command("runserver", Server(
        use_debugger=True,
        use_reloader=True,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 5000))))

