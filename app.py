from main import create_app
from flask import g

app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)


@app.teardown_request
def teardown_request(exception=None):
    # Close the SQLAlchemy session if it exists
    if hasattr(g, 'db_session'):
        try:
            g.db_session.close()
        except Exception as e:
            # Handle any exception that occurs while closing the session
            print("An error occurred while closing the session:", e)