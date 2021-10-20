from orator.migrations import Migration


class CreateJobsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('jobs') as table:
            table.increments('id')
            table.string('jobs_title')
            table.string('jobs_desc')
            table.string('min_qualifications')
            table.string('jobs_level')
            table.string('jobs_category')
            table.string('edu_background')
            table.string('count_vacancy')
            table.integer('companies_id', unsigned=True)
            table.timestamps()
            table.foreign('companies_id').references('id').on('companies')
            table.datetime('expired_post')



    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('jobs')
