# Taskbuster

Code for [Taskbuster Django Tutorial](http://www.marinamele.com/taskbuster-django-tutorial)

## Development
### Requirements

Requirements can be found in the `requirements` folder.

```bash
pip install -r requirements/development.txt
```

### Secret Key and Settings

Specify `SECRET_KEY` and `DJANGO_SETTINGS_MODULE` environment variables.
Different settings can be found in the `taskbuster.settings` folder.

```bash
export SECRET_KEY="..."
export DJANGO_SETTINGS_MODULE="taskbuster.settings.development"
```
