# URLShot

Take a screenshot of URL using API

> Unfortunately, Vercel does not support this type of application.

## To locally execute the project

Clone this repository:

```shell
git clone https://github.com/kremilly/URLShot
```

Install the dependencies:

```shell
pip install -r requirements.txt
```

To run the server, use:

```shell
python index.py
```

> ***IMPORTANT***: Download and Install the EdgeDriver, you can download this [link](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?ch=1&form=MA13LH#downloads)

### Example of request

```shell
http://127.0.0.1:5000/api?url=https://example.com&width=1920&height=1080
```

### Queries Parameters

* `url` URL to take a screenshot
* `width` Width of image
* `height` Height of image

## Dependencies

* Python
* Flask
* selenium
* EdgeDriver
* requests
