Taskbuster
==========

Code for |taskbuster_tutorial|.

.. |taskbuster_tutorial| raw:: html

    <a href="http://www.marinamele.com/taskbuster-django-tutorial" target="_blank">Taskbuster Django Tutorial</a>

Development
-----------

Requirements
~~~~~~~~~~~~

Requirements can be found in the `requirements` folder.

    pip install -r requirements/development.txt

Secret Key and Settings
~~~~~~~~~~~~~~~~~~~~~~~

Specify `SECRET_KEY` and `DJANGO_SETTINGS_MODULE` environment variables.
Different settings can be found in the `taskbuster.settings` folder.

    export SECRET_KEY="..."
    export DJANGO_SETTINGS_MODULE="taskbuster.settings.development"

Coverage
~~~~~~~~

Run coverage tool:

    coverage run --source='.' manage.py test

Console report:

    coverage report

Generate HTML report (`htmlcov/index.html`):

    coverage html
