An example project is included in the repo's `example` directory.


## Set-up

To run the example project:

```bash
# Enter the example directory
cd example

# Install the dependencies (in a virtual environment, ideally)
pip install -r requirements.txt

# Transpile the validators from Python to JavaScript

./manage.py transpile_validators

# Run the server
./manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to view a form with a number of validator functions.

## Demo

![Example project form with JS validators gif](./media/django-front-end-validators.gif)
