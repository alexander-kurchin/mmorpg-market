from django_filters import FilterSet, ModelChoiceFilter

from .models import AdvertModel, ReplyModel


def advert_list(request):
    if request is None:
        return AdvertModel.objects.all()
    return AdvertModel.objects.filter(user=request.user)


class ReplyModelFilterSet(FilterSet):
    advert = ModelChoiceFilter(empty_label='All',
                               queryset=advert_list)

    class Meta:
        model = ReplyModel
        fields = ['advert']
