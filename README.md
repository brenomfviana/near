# Near

## Introduction

NEAR is a Web Service that provides operations related to a chat with simultaneous translation of messages context.

It aims to be RESTful (Representational State Transfer) and it uses Python with Flask in its implementation.

## Features and TO-DOs

- [x] Rolling a dice of any faces through /rtd/<number of dice's faces>;
- [x] Performing the translation of a message through /translate (via POST);
- [ ] Database usage;
- [ ] Use this API in Omega.

## Setting things up

Requirements:

* Python 3;
* Python pip.

To fetch all dependencies of this project, go to it's root folder, through terminal, and type:

```
pip install -r requirements.txt
```

## Running as it is and trying it out

Go to the root of the project, through terminal, and type:

```
python run.py
```

It will start listening at localhost:5000 (I guess). Go to localhost:5000/rtd/6 to test it. The result may be a JSON containing { 'response' : <Random number between 1 and 6> }

## Team

[<img src="https://avatars2.githubusercontent.com/u/17532418?v=3&s=400" width="100"/>](https://github.com/brenov) | [<img src="https://avatars1.githubusercontent.com/u/6081758?s=400&v=4" width="100"/>](https://github.com/murilobnt)
---|---
[Breno Viana](https://github.com/brenov) | [Murilo Bento](https://github.com/murilobnt)
