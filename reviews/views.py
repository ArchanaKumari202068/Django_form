from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView

# from django.shortcuts import render

from .forms import ReviewForm
from .models import Review




class ReviewView(CreateView):

    model=Review
    form_class= ReviewForm
    template_name ="reviews/review.html"
    success_url= "/thank-you"





    # def get(self,request):
    #     form = ReviewForm()

    #     return render(request,"reviews/review.html", {
    #         "form": form
    #     })
    
    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    #     return render(request,"reviews/review.html", {
    #         "form": form
    #     })


# Create your views here.

# def review(request):

#     if request.method =='POST':
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
    
#     return render(request, "reviews/review.html",{
#         "form":form
# })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["message"]= "This works!"
        return context
    # def get(self,request):

    #     return render(request,"reviews/thank_you.html")


#list view for fetching list of data    

class ReviewsListView(ListView):
    template_name="reviews/review_list.html"
    model =Review
    context_object_name = "reviews"

    # reviews greater than 4


    # def get_queryset(self):
    #     base_query=super().get_queryset()
    #     data =base_query.filter(rating__gt=4)
    #     return data


  

    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     reviews=Review.objects.all()
    #     context["reviews"]= reviews
    #     return context


    
class SingleReviewView(DetailView):
    template_name= "reviews/single_review.html"
    model = Review
    # context_object_name = "reviews"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


    # def get_context_data(self, **kwargs):

    #     context= super().get_context_data(**kwargs)
    #     review_id= kwargs["id"]
    #     selected_reviews = Review.objects.get(pk=review_id)
    #     context['reviews']= selected_reviews
    #     return context
   

   #session

  

class AddFavoriteView(View):
    def post(self,request):
        review_id = request.POST['review_id']
        request.session["favorite_review"] = review_id # store in session
        return HttpResponseRedirect("/reviews/" + review_id)
 