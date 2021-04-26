from app import *
from app.config.AppConfig import *

server_port = FlaskConfig.PORT
print(server_port)
app.run(host="0.0.0.0", port=server_port)
# a()


# TODO 
# 1.controller useing by read_by_email method
# 2.jwt check