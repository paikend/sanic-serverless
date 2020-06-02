from sanic import Sanic
from sanic.response import text
from mangum import Mangum
from middlewares.base import CorsMiddleware

app = Sanic(__name__)
CorsMiddleware(app)

@app.route("/")
async def hello_bigpearl(request):
  return text("""
                          ▄▄▄▄▄                  _________________
                          ▀▀▀██████▄▄▄          /  paikend!       \\
                        ▄▄▄▄▄  █████████▄       |  Gotta go fast! |
                        ▀▀▀▀█████▌ ▀▐▄ ▀▐█      | ________________/
                      ▀▀█████▄▄ ▀██████▄██      |/ 
                      ▀▄▄▄▄▄  ▀▀█▄▀█════█▀         
                          ▀▀▀▄  ▀▀███ ▀      ▄▄   
                        ▄███▀▀██▄████████▄ ▄▀▀▀██▌ 
                      ██▀▄▄▄██▀▄███▀ ▀▀████     ▀█▄
                  ▄▀▀▀▄██▄▀▀▌████▒▒▒▒▒▒███    ▌▄▄▀
                  ▌    ▐▀████▐███▒▒▒▒▒▐██▌        
                  ▀▄  ▄▀   ▀▀████▒▒▒▒▄██▀         
                    ▀▀      ▀▀█████████▀          
                          ▄▄██▀██████▀█           
                        ▄██▀     ▀▀▀  █           
                        ▄█             ▐▌          
                    ▄▄▄▄█▌              ▀█▄▄▄▄▀▀▄  
                  ▌     ▐                ▀▀▄▄▄▀   
                    ▀▀▄▄▀                          
  """)

handler = Mangum(app)

if __name__ == '__main__':
  app.run(host="127.0.0.1", port=4000, auto_reload=True)
