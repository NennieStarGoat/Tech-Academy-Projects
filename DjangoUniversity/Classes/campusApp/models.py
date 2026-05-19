from django.db import models

# Model of University Campus


class UniversityCampus(models.Model):
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(null=True, blank=True, default="")

    # Model Manager

    object = models.Manager()

    # Displays object output values in the form of a string
    def __str__(self):
        # Returns input value of the campus name to display in the browser instead of the default titles
        display_campus = '{0.name}'
        return display_campus.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
