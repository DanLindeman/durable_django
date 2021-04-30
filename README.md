# Durable + Django

Install and run the demo

Language setup

```
echo "layout poetry" >> .envrc
asdf local python 3.9.2
```

```
poetry install
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Navigate to:
http://localhost:8000/rules/

Observe the log

> Somebody said hello

http://localhost:8000/rules/Tony/

Observe the log

> Somebody said Tony

http://localhost:8000/rules/idk-someone-else/

> 404 Not Found

## How it works

The rules engine creates a host which Views can `host.post` to. These rules are evaluated when posting a fact to the ruleset.

Upon finding a matching rule, a Django signal is sent, which can be received from another receiver function. The receiver is what prints the message. The view that caused the rule to fire only sees the result of posting the fact to the rules, the consequences are carried out elsewhere.
