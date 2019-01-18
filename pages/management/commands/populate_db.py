from django.core.management.base import BaseCommand
from pathlib import Path
import pandas as pd

from pages.models import Salary


class Command(BaseCommand):
    help = "A command to manually insert data from CVS file to the database"

    def add_arguments(self, parser):
        parser.add_argument('input_file')

    def handle(self, *args, **options):
        file_name = options['input_file']
        file_path = Path(__file__).parents[3].joinpath(file_name)
        salary_df = pd.read_csv(file_path)
        for index, row in salary_df.iterrows():
            Salary.objects.update_or_create(years=row['workedYears'], salary=row['salaryBrutto'])