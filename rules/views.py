import django.dispatch
from django.dispatch import receiver
from durable.engine import MessageNotHandledException
from durable.lang import get_host, m, ruleset, when_all
from rest_framework import views
from rest_framework.response import Response

with ruleset("test"):
    # antecedent
    @when_all(m.subject == "World")
    def say_hello(con):
        # consequent
        pizza_done.send(sender="say_hello", toppings=["garlic", "roma"], size="large")

    # antecedent
    @when_all(m.subject == "Tony")
    def say_tony(con):
        # consequent
        pizza_done.send(sender="say_tony", toppings=["pepperoni"], size="personal")


host = get_host()
pizza_done = django.dispatch.Signal()


@receiver(pizza_done, sender="say_hello")
def hello_handler(sender, **kwargs):
    print("Somebody said hello")


@receiver(pizza_done, sender="say_tony")
def tony_handler(sender, **kwargs):
    print("Somebody said Tony")


class RuleView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            res = host.post("test", {"subject": "World"})
            return Response({"data": res}, status=200)
        except MessageNotHandledException:
            return Response({"message": "Not Found"}, 404)


class RuleDetailView(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            res = host.post("test", {"subject": pk})
            return Response({"data": res}, status=200)
        except MessageNotHandledException:
            return Response({"message": "Not Found"}, 404)
