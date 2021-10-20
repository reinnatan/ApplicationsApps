from orator.migrations import Migration


class CreateApplicationsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('applications') as table:
            table.increments('id')
            table.string('status')
            table.integer('applicants_id', unsigned=True)
            table.integer('jobs_id', unsigned=True)
            table.foreign('applicants_id').references('id').on('jobs')
            table.foreign('jobs_id').references('id').on('jobs')
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('applicantions')
