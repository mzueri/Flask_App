from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5000) 
    # recall that localhost has IP Address 127.0.0.1.
    # We set the host to "0.0.0.0" because otherwise we could not start the app from our machine when running a docker container.
    # This makes it possible for Docker to map traffic from your host machine to the container port.
    # port defines the port where the data from the requests comes through.
