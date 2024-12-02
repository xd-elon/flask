from flask import Flask, request, jsonify
from schema import graphql_schema  # Importa o schema configurado

app = Flask(__name__)

@app.route("/graphql", methods=["POST"])
def graphql_server():
    from ariadne import graphql_sync
    data = request.get_json()
    success, result = graphql_sync(graphql_schema, data)
    return jsonify(result)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/static/css/index.css" />
        <script src="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/static/js/middleware.js"></script>
    </head>
    <body>
        <div id="root"></div>
        <script>window.addEventListener('load', function (event) { GraphQLPlayground.init(document.getElementById('root'), { endpoint: '/graphql' }) })</script>
    </body>
    </html>
    """, 200

if __name__ == "__main__":
    app.run(debug=True)
