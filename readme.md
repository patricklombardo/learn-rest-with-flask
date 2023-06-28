# Introduction to REST Architecture with Flask & Python

This is my attempt at a simple and useful introduction to RESTful services. Please note that this is designed from an engineer's perspective, and is in no way comprehensive. For more comprehensive information, please see the documentation linked at the bottom.

## What is REST
REST stands for REpresentation State Transfer and is a protocol used to communicate information over the Internet via HTTP. Any time you use a web browser to visit a website, there is a very good chance information is being transferred over REST protocol.

A service, such as an API, is said to be *RESTful* if it conforms to the REST specification.

### REST Architectural Constraints
REST by definition has the following architectural constraints, which have the end goal of improving performance
1. *Client-Server Architecture* paradigm 
2. *Statelessness* - each request is discrete and isolated; no session is saved between requests
3. *Cacheability* - responses may be cached where appropriate
4. *Layered System* - a client should not be able to tell whether it is connected directly to the server or behind a proxy
5. *Code on Demand* (optional) - Ability for client-side scripting (e.x. React apps)
6. *Uniform Interface* - Each REST endpoint has a common request and response design

For more information, see the [Wikipedia article](https://en.wikipedia.org/wiki/Representational_state_transfer#Architectural_constraints).

### Data Transfer Over the Internet
![REST Client-Server Architecture](./assets/rest_client_server_arch.jpeg)

REST architecture uses a Request/Response paradigm where a **Client** sends a request to a **resource** on a REST API server, and the server sends a response that is *REpresentative* of the *State*, which is then *Transferred* to the client (hence **REST**!)

A REST API can be used to represent states of many different things and can contain lots of complex underlying logic. Some examples may include:
- Databases (Postgres, MongoDB, etc.)
- ML Algorithms
- EMR Jobs
- And even other REST services

### Rest Requests and Responses
![REST Request and Response Format](./assets/rest_request_response.jpeg)
REST Requests and Responses have certain elements to them that are necessary for the receiving service to understand the intent of the request,

**Requests** Contain:
- *method* - `GET`, `POST`, `PUT`, or `DELETE` (note: there are others that I will not discuss here), are the basic CRUD operations that describe what the client is trying to do to the resource (i.e. `GET` information, `POST` (create) a new resource, etc.)
- *uri* - the address of the resource, unique on the server (and on the internet). Where are you sending the request?
- *headers* - metadata about the request. For example, what data type is in the body (JSON, HTML, MIME media), authentication tokens.
- *body* - the meat of the request, the data. This may be in many formats, but in most use cases you can expect to see JSON.

**Responses** Contain:
- *Status Codes* - give information about how the request processing went. Some common ones are 200, 404, and 500. Generally, we want to see 200s.
- *headers* - same as above
- *body* - same as above

### Serialization and Deserialization
Data sent over REST often needs to be *serialized* upon sending and *deserialized* on the receiving side. This is because REST services send data in a serial format - this can be thought of as one long string, character by character.

JSON has become the standard for sending data over REST API requests (of course, other XML-like languages are also easily serialized). Note that JSON is a *representation* of the the client's state distinct from the internal state itself.  This was a convenient choice, as JSON stands for JavaScript Object Notation, and is the native data structure for front-end web applications. However, this also presents a problem, as JSON has a limited number of data types. This means it is not "round-trip" safe. For example, a `datetime` object in python has no comparable type in JSON, and would need to be serialized in a JSON compatible format, such as an ISO Timestamp String, then parsed on the receiving end.

This is where many libraries such as [Pydantic](https://github.com/pydantic/pydantic), [Marshmallow](https://marshmallow.readthedocs.io/en/stable/), and [Immutables](https://immutables.github.io) come in to define data models.

## Running the Application
The application in this repo is a simple Flask app that illustrates the four key rest methods.

The application is a simple API for managing desserts. It is "dumb" in that there is no validation or complications.
The desserts are loaded into memory from the `database.json` file; therefore, changes are not persisted, which is perfectly fine for our purposes. 

You can think of the "database" as the python dictionary containing these in memory within the service. Note that dictionary is the *internal state*: to access and mutate this state from outside the application, we have created endpoints for each operation. Each kind of operation is a *resource* on the server; each resource has its own endpoint.

### Prerequisites
1. Python 3.10
2. [Postman](https://www.postman.com) is recommended to use the attached collection

### Getting Started
Create a virtual environment and install the requirements
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running the application
The following will run the app on port `8080`
```bash
flask --app api.app run -p 8080
```

### Endpoints
- `GET /` - Retrieves all the desserts in memory
- `GET /<id>` - Retrieves the dessert with the given ID
    - *Note: this will fail if the ID does not exist*
- `POST /<id>` - Creates a new dessert with a given ID
    - *Note: this will fail if the ID already exists*
- `PUT /<id>` - Updated a dessert with a given ID
    - *Note: this will fail if the ID doesn't exist*
- `DELETE /<id>` - Deletes the dessert with the given ID

### Postman
You can import the collection in this repository to Postman and interact with the endpoints. Something to notice: as you add and update desserts, compare the response of `GET /` to `database.json`. The *internal state* of the application will be different from the contents of the json file.

## Additional Documentation
- [MDN HTTP Response Status Codes Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [MDN HTTP Reference Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [RFC 9110 - HTTP Semantics](https://httpwg.org/specs/rfc9110.html#REST)
- [Wikipedia - Representational State Transfer](https://en.wikipedia.org/wiki/Representational_state_transfer#Architectural_constraints)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/)
