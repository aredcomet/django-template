import json
import os
from typing import Any, Optional

from django.contrib.auth.hashers import make_password
from django.core.management.base import (BaseCommand, CommandError,
                                         CommandParser)

PASSWORD = os.getenv('DUMMY_PASSWORD')

dataset = [
]


class Command(BaseCommand):
    help = "generate users"

    def add_arguments(self, parser: CommandParser) -> None:
        pass

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        output_fp = "core/fixtures/user.json"
        ## TODO generate fields here here
        data = [
            {
                "model": "core.user",
                "pk": x+1,
                "fields": {
                    "password": make_password(PASSWORD),
                    **dataset[x],
                }
            }
            for x in range(len(dataset))
        ]
        with open(output_fp, "wt") as fp:
            json.dump(data, fp)
        self.stdout.write(self.style.SUCCESS("Successfully generated fixture"))

