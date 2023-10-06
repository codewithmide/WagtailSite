from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from django import forms
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


# This class defines a method called get_context that takes in two parameters: self and request.
# Inside the method, it first calls the get_context method of the superclass to get the initial context.
# Then, it retrieves a list of published blog pages, ordered by their first publication date in reverse chronological order.
# Finally, it adds the list of blog pages to the context dictionary and returns the updated context.
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    # add the get_context method:
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
    
    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

# This code snippet defines a method called main_image that belongs to a class. It retrieves the first gallery image from a collection of gallery images. If there is a gallery image, it returns the image. Otherwise, it returns None.
class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=500)
    body = RichTextField(blank=True)
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    authors = ParentalManyToManyField('blog.Author', blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)


    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
            FieldPanel('tags'),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

# This code snippet defines a model called BlogPageGalleryImage that extends the model BlogPage. It defines a method called image that retrieves the first image from a collection of gallery images.
class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

# This code snippet defines a model called Author that extends the model Page. It defines a method called __str__ that returns the name of the author.
@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('author_image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'


# This code snippet defines a model called BlogTagIndexPage that extends the model Page. It defines a method called get_context that takes in two parameters: self and request.
# The method retrieves the value of the tag parameter from the request's query parameters. It then filters the BlogPage objects based on the value of the tag parameter.
# The method then calls the get_context method of the parent class (assuming there is one) and assigns the returned context to a variable called context. Finally, it adds the filtered blogpages to the context
class BlogTagIndexPage(Page):
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context