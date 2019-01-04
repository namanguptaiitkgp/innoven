from django.shortcuts import render
from django.views import generic
# Create your views here.
from projects.models import Project, Stage, Sector, Engagement, Member, Partner, Investor, Dialouge
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_projects = Project.objects.all().count()
    stage = Stage.objects.all()
    sector = Sector.objects.all()
    engagement = Engagement.objects.all()
    num_member = Member.objects.all().count()
    investor = Investor.objects.all()
    context = {
        'num_projects': num_projects,
        'num_member':num_member,
        'stage_list':stage,
        'sector_list':sector,
        'engagement_list':engagement,
        'investor_list':investor,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.db.models import Q
from django.contrib.postgres.search import SearchVector
def Search(request):
    query = request.GET.get('q')
    results = Project.objects.filter(Q(description__icontains=query) |Q(sector__name__icontains=query) |  Q(name__icontains=query) | Q(competitor__icontains=query) | Q(investor__icontains=query))
    context = {'project_list':results}
    return render(request, 'projects/search_projects.html' , context = context)

def Allprojects(request):

    result1 = Project.objects.filter(Q(engagement__engagement_name__icontains="Level 1"))
    result2 = Project.objects.filter(Q(engagement__engagement_name__icontains="Level 2"))
    result3 = Project.objects.filter(Q(engagement__engagement_name__icontains="Level 3"))
    context = {'project_list1':result1,'project_list2':result2,'project_list3':result3}
    return render(request, 'projects/all_projects.html' , context = context)

def MySearch(request):
    stage = request.GET.get('mystage')
    engagement = request.GET.get('myengagement')
    sector = request.GET.get('mysector')
    investor = request.GET.get('myinvestor')

    if (stage == 'any') & (sector == 'any') & (engagement == 'any') & (investor == 'any'):
        results = Project.objects.all()
    elif (sector == 'any') & (engagement == 'any')& (investor == 'any'):
        results = Project.objects.filter(stage__stage_name=stage)
    elif (stage == 'any') & (engagement == 'any')& (investor == 'any'):
        results = Project.objects.filter(sector__name=sector)
    elif (sector == 'any') & (stage == 'any')& (investor == 'any'):
        results = Project.objects.filter(engagement__engagement_name=engagement)
    elif (sector == 'any') & (engagement == 'any')& (stage == 'any'):
        results = Project.objects.filter(investor__name=investor)
    elif (stage == 'any')& (investor == 'any') :
        results = Project.objects.filter(engagement__engagement_name=engagement,sector__name=sector)
    elif (engagement == 'any') & (investor == 'any'):
        results = Project.objects.filter(stage__stage_name=stage, sector__name=sector)
    elif (sector == 'any')& (investor == 'any'):
        results = Project.objects.filter(engagement__engagement_name=engagement, sector__name=sector)
    elif (stage == 'any')& (engagement == 'any') :
        results = Project.objects.filter(investor__name=investor,sector__name=sector)
    elif (engagement == 'any') & (sector == 'any'):
        results = Project.objects.filter(stage__stage_name=stage,investor__name=investor)
    elif (sector == 'any')& (stage == 'any'):
        results = Project.objects.filter(engagement__engagement_name=engagement, investor__name=investor)
    elif stage == 'any' :
        results = Project.objects.filter(engagement__engagement_name=engagement,sector__name=sector, investor__name=investor)
    elif engagement == 'any':
        results = Project.objects.filter(stage__stage_name=stage, sector__name=sector, investor__name=investor)
    elif sector == 'any':
        results = Project.objects.filter(engagement__engagement_name=engagement, sector__name=sector, investor__name=investor)
    elif investor == 'any':
        results = Project.objects.filter(engagement__engagement_name=engagement, sector__name=sector,stage__stage_name=stage )
    else:
        results = Project.objects.filter(stage__stage_name=stage, engagement__engagement_name=engagement,sector__name=sector,investor__name=investor)

    context = {'project_list':results}
    return render(request, 'projects/search_projects.html' , context = context)



class ProjectListView(generic.ListView):
    model = Project
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProjectListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

    paginate_by = 10

class ProjectDetailView(generic.DetailView):
    model = Project

class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'


class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects')



class PartnerListView(generic.ListView):
    model = Partner
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PartnerListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

    paginate_by = 10

class PartnerDetailView(generic.DetailView):
    model = Partner

class PartnerCreate(CreateView):
    model = Partner
    fields = '__all__'


class PartnerUpdate(UpdateView):
    model = Partner
    fields = '__all__'

class PartnerDelete(DeleteView):
    model = Partner
    success_url = reverse_lazy('partner')


from projects.models import Investor

class InvestorListView(generic.ListView):
    """
    Generic class-based list view for a list of authors.
    """
    model = Investor
    paginate_by = 10


class InvestorDetailView(generic.DetailView):
    """
    Generic class-based detail view for an author.
    """
    model = Investor

class InvestorCreate(CreateView):
    model = Investor
    fields = '__all__'
    initial = {'description': 'Main focus of the fund'}

class InvestorUpdate(UpdateView):
    model = Investor
    fields = ['name', 'fund_size', 'description']

from .forms import add_dialouge
from django.shortcuts import redirect

def dialouge_new(request):
    if request.method == "POST":
        form = add_dialouge(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_projects')
    else:
        form = add_dialouge()
    return render(request, 'projects/dialouge_form.html', {'form': form})

from .forms import add_doc

class DialougeDelete(DeleteView):
    model = Dialouge
    success_url = reverse_lazy('all_projects')

def doc_new(request):
    if request.method == "POST":
        form = add_doc(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_projects')
    else:
        form = add_doc()
    return render(request, 'projects/doc_form.html', {'form': form})