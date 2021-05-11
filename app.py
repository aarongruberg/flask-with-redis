
# Added imports for redis
from flask import Flask, render_template
#import redis

app = Flask(__name__)

# Added redis database connection test
# try:
#     conn = redis.StrictRedis(
#         host='redis-test-kris',
#         port=10000)
#         #password='YOUR_PASSWORD')
#
#     #print(conn)
#     app.logger.info('connecting')
#     app.logger.info(conn)
#     conn.ping()
#     print('Connected!')
# except Exception as ex:
#     print('Error:', ex)
#     exit('Failed to connect, terminating.')

raise Exception('Oops')


@app.route('/')
def index():
    return render_template('index.html')

# testing this function
app.run()
