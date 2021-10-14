from django.views import generic

from articles.models import Article, Tag


class ArticleListView(generic.ListView):
    model = Article
    context_object_name = 'articles_list'
    queryset = Article.objects.all()
    template_name = 'article/articles_list.html'

    def get_queryset(self):
        articles = Article.objects.all()
        if self.request.GET:
            query = dict(self.request.GET)
            tag = query.get('tag')
            tag = tag[0] if tag else None
            tags = Tag.objects.filter(name=tag).values_list('id', flat=True)
            return articles.filter(tags__id__in=tags)
        return articles

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()[:10]
        return context

class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'article/article_detail.html'





