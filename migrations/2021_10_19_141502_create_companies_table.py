from orator.migrations import Migration


class CreateCompaniesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('companies') as table:
            table.increments('id')
            table.string('email')
            table.string('password')
            table.string('name')
            table.string('desc')
            table.string('address')
            table.string('website_url')
            table.boolean('is_active')
            table.string('token')
            table.timestamps()
            table.datetime('expired_token')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('companies')
