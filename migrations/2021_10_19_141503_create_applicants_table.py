from orator.migrations import Migration


class CreateApplicantsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('applicants') as table:
            table.increments('id')
            table.string('email')
            table.string('password')
            table.string('name')
            table.string('address')
            table.string('phone')
            table.string('token')
            table.timestamps()
            table.datetime('expired_token')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('applicants')
