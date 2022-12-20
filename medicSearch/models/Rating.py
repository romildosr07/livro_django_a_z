from medicSearch.models import *


class Rating(models.Model):
    user = models.foreignKey(User, null=True, related_name='avaliou', on_delete=models.CASCADE)
    user_rated = models.foreignKey(User, null=True, related_name='avaliado', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_place=2)
    opinion = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Avaliador: {} | Avaliado: {}'.format(self.user.first_name, self.user_rated)
