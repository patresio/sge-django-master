from django.core.management.base import BaseCommand

from ai.agent import SGEAgent


class Command(BaseCommand):
    help = "Invoke SGE Agent"

    def handle(self, *args, **options):
        agent = SGEAgent()
        agent.invoke()

        self.stdout.write(self.style.SUCCESS("SGE Agent invoked successfully."))
