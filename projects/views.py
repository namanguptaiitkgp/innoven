from django.shortcuts import render
from django.views import generic
# Create your views here.
from projects.models import Project, Stage, Sector, Engagement, Member, Partner, Investor, Dialouge, DealStage , OStatus, Director, Pcompanies
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_projects = Project.objects.all().count()
    stage = Stage.objects.all()
    dealstage = DealStage.objects.filter(~Q(name="Early"))
    ostatus = OStatus.objects.all()
    member = Member.objects.all()
    director = Director.objects.all()
    engagement = Engagement.objects.all()
    num_member = Member.objects.all().count()
    investor = Investor.objects.all()
    sector = Sector.objects.all()

    context = {
        'num_projects': num_projects,
        'num_member':num_member,
        'stage_list':stage,
        'member_list':member,
        'director_list': director,
        'engagement_list':engagement,
        'investor_list':investor,
        'dealstage_list':dealstage,
        'ostatus_list':ostatus,
        'sector_list': sector,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.db.models import Q
from django.contrib.postgres.search import SearchVector

def Search(request):
    query = request.GET.get('q')
    results = Project.objects.filter(Q(description__icontains=query) |Q(sector__name__icontains=query) |  Q(name__icontains=query) | Q(competitor__name__icontains=query) | Q(investor__name__icontains=query) | Q(partner__name__icontains=query)).distinct()
    context = {'project_list':results}
    return render(request, 'projects/search_projects.html' , context = context)

def Engprojects(request):
    result0 = Project.objects.filter(Q(engagement__engagement_name__icontains="Level 0") & Q(overall_Status__name="Active") )
    result1 = Project.objects.filter(Q(engagement__engagement_name__icontains="Level 1") & Q(overall_Status__name="Active") )
    result2 = Project.objects.filter(Q(engagement__engagement_name__icontains="Level 2") & Q(overall_Status__name="Active") )
    result3 = Project.objects.filter(Q(engagement__engagement_name__icontains="Level 3") & Q(overall_Status__name="Active") )
    context = {'project_list0': result0, 'project_list1': result1, 'project_list2': result2, 'project_list3': result3}

    return render(request, 'projects/engagement_projects.html', context=context)


def Myprojects(request):
    ds00 = Project.objects.filter(Q(dealstage__name__icontains="Early")& Q(overall_Status__name="Active")  & Q(engagement__engagement_name__icontains="Level 0"))
    ds01 = Project.objects.filter(Q(dealstage__name__icontains="Early") & Q(overall_Status__name="Active") & Q(engagement__engagement_name__icontains="Level 1"))
    ds02 = Project.objects.filter(Q(dealstage__name__icontains="Early") & Q(overall_Status__name="Active") & Q(engagement__engagement_name__icontains="Level 2"))
    ds03 = Project.objects.filter(Q(dealstage__name__icontains="Early") & Q(overall_Status__name="Active") & Q(engagement__engagement_name__icontains="Level 3"))

    ds10 = Project.objects.filter(Q(dealstage__name__icontains="Prospect")& Q(overall_Status__name="Active") & Q(engagement__engagement_name__icontains="Level 0"))
    ds11 = Project.objects.filter(Q(dealstage__name__icontains="Prospect") & Q(overall_Status__name="Active") & Q(engagement__engagement_name__icontains="Level 1"))
    ds12 = Project.objects.filter(Q(dealstage__name__icontains="Prospect") & Q(overall_Status__name="Active") & Q(engagement__engagement_name__icontains="Level 2"))
    ds13 = Project.objects.filter(Q(dealstage__name__icontains="Prospect") & Q(overall_Status__name="Active") & Q(engagement__engagement_name__icontains="Level 3"))

    ds2 = Project.objects.filter(Q(dealstage__name__icontains="Underwriting Stage")& Q(overall_Status__name="Active") )
    ds3 = Project.objects.filter(Q(dealstage__name__icontains="TS Issued")& Q(overall_Status__name="Active") )
    ds4 = Project.objects.filter(Q(dealstage__name__icontains="TS Closure")& Q(overall_Status__name="Active") )
    ds5 = Project.objects.filter(Q(dealstage__name__icontains="Documentation")& Q(overall_Status__name="Active") )
    ds6 = Project.objects.filter(Q(overall_Status__name="On Hold"))
    ds7 = Project.objects.filter(Q(overall_Status__name="Lost"))
    context = {'ds00':ds00,'ds01':ds01,'ds02':ds02,'ds03':ds03,'ds10':ds10,'ds11':ds11,'ds12':ds12,'ds13':ds13,'ds2':ds2,'ds3':ds3,'ds4':ds4,'ds5':ds5,'ds6':ds6,'ds7':ds7}
    return render(request, 'projects/my_projects.html' , context = context)

def Allprojects(request):
    ds0 = Project.objects.filter(Q(dealstage__name__icontains="Early") & Q(overall_Status__name="Active") )
    ds1 = Project.objects.filter(Q(dealstage__name__icontains="Prospect") & Q(overall_Status__name="Active") )
    ds2 = Project.objects.filter(Q(dealstage__name__icontains="Underwriting Stage") & Q(overall_Status__name="Active") )
    ds3 = Project.objects.filter(Q(dealstage__name__icontains="TS Issued") & Q(overall_Status__name="Active") )
    ds4 = Project.objects.filter(Q(dealstage__name__icontains="TS Closure") & Q(overall_Status__name="Active") )
    ds5 = Project.objects.filter(Q(dealstage__name__icontains="Documentation") & Q(overall_Status__name="Active") )
    ds6 = Project.objects.filter(Q(overall_Status__name="On Hold"))
    ds7 = Project.objects.filter(Q(overall_Status__name="Lost"))
    context = {'ds0': ds0, 'ds1': ds1, 'ds2': ds2, 'ds3': ds3, 'ds4': ds4, 'ds5': ds5,'ds6':ds6,'ds7':ds7}
    return render(request, 'projects/all_projects.html', context=context)

def MySearch(request):
    stage = request.GET.get('mystage')
    engagement = request.GET.get('myengagement')
    member = request.GET.get('mymember')
    investor = request.GET.get('myinvestor')

    if (stage == 'any') & (member == 'any') & (engagement == 'any') & (investor == 'any'):
        results = Project.objects.all()
    elif (member == 'any') & (engagement == 'any')& (investor == 'any'):
        results = Project.objects.filter(funding_Round__stage_name=stage)
    elif (stage == 'any') & (engagement == 'any')& (investor == 'any'):
        results = Project.objects.filter(member__name=member)
    elif (member == 'any') & (stage == 'any')& (investor == 'any'):
        results = Project.objects.filter(engagement__engagement_name=engagement)
    elif (member == 'any') & (engagement == 'any')& (stage == 'any'):
        results = Project.objects.filter(investor__name=investor)
    elif (stage == 'any')& (investor == 'any') :
        results = Project.objects.filter(engagement__engagement_name=engagement,member__name=member)
    elif (engagement == 'any') & (investor == 'any'):
        results = Project.objects.filter(funding_Round__stage_name=stage, member__name=member)
    elif (member == 'any')& (investor == 'any'):
        results = Project.objects.filter(engagement__engagement_name=engagement, member__name=member)
    elif (stage == 'any')& (engagement == 'any') :
        results = Project.objects.filter(investor__name=investor,member__name=member)
    elif (engagement == 'any') & (member == 'any'):
        results = Project.objects.filter(funding_Round__stage_name=stage,investor__name=investor)
    elif (member == 'any')& (stage == 'any'):
        results = Project.objects.filter(engagement__engagement_name=engagement, investor__name=investor)
    elif stage == 'any' :
        results = Project.objects.filter(engagement__engagement_name=engagement,member__name=member, investor__name=investor)
    elif engagement == 'any':
        results = Project.objects.filter(funding_Round__stage_name=stage, member__name=member, investor__name=investor)
    elif member == 'any':
        results = Project.objects.filter(engagement__engagement_name=engagement, member__name=member, investor__name=investor)
    elif investor == 'any':
        results = Project.objects.filter(engagement__engagement_name=engagement, member__name=member,funding_Round__stage_name=stage )
    else:
        results = Project.objects.filter(funding_Round__stage_name=stage, engagement__engagement_name=engagement,member__name=member,investor__name=investor)

    context = {'project_list':results}
    return render(request, 'projects/search_projects.html' , context = context)

def MyKeySearch(request):
    dealstage = request.GET.get('mydealstage')
    ostatus = request.GET.get('myostatus')
    member = request.GET.get('mymember')
    director = request.GET.get('mydirector')

    if (dealstage == 'any') & (member == 'any') & (ostatus == 'any') & (director == 'any'):
        results = Project.objects.filter(~Q(dealstage__name="Early") )

    elif (member == 'any') & (ostatus == 'any') & (director == 'any'):
        results = Project.objects.filter(Q(dealstage__name=dealstage)  )

    elif (dealstage == 'any') & (ostatus == 'any') & (director == 'any'):
        results = Project.objects.filter(Q(member__name=member) & ~Q(dealstage__name="Early") )

    elif (member == 'any') & (dealstage == 'any') & (director == 'any'):
        results = Project.objects.filter(Q(overall_Status__name=ostatus) & ~Q(dealstage__name="Early"))

    elif (member == 'any') & (ostatus == 'any') & (dealstage == 'any'):
        results = Project.objects.filter(Q(director__name=director) & ~Q(dealstage__name="Early"))

    elif (dealstage == 'any') & (director == 'any'):
        results = Project.objects.filter(Q(overall_Status__name=ostatus) & Q(member__name=member) & ~Q(dealstage__name="Early"))
    elif (ostatus == 'any') & (director == 'any'):
        results = Project.objects.filter(Q(dealstage__name=dealstage) & Q(member__name=member) )
    elif (member == 'any') & (director == 'any'):
        results = Project.objects.filter(Q(overall_Status__name=ostatus) & Q(member__name=member))
    elif (dealstage == 'any') & (ostatus == 'any'):
        results = Project.objects.filter(Q(director__name=director) & Q(member__name=member) & ~Q(dealstage__name="Early") )
    elif (ostatus == 'any') & (member == 'any'):
        results = Project.objects.filter(Q(dealstage__name=dealstage) & Q(director__name=director))
    elif (member == 'any') & (dealstage == 'any'):
        results = Project.objects.filter(Q(overall_Status__name=ostatus) & Q(director__name=director))
    elif dealstage == 'any':
        results = Project.objects.filter(Q(overall_Status__name=ostatus) & Q(member__name=member) & Q(director__name = director) & ~Q(dealstage__name="Early"))
    elif ostatus == 'any':
        results = Project.objects.filter(Q(dealstage__name=dealstage) & Q(member__name=member) & Q(director__name=director)  )
    elif member == 'any':
        results = Project.objects.filter(Q(overall_Status__name=ostatus) & Q(dealstage__name=dealstage) & Q(director__name=director))
    elif director == 'any':
        results = Project.objects.filter(Q(overall_Status__name=ostatus) & Q(member__name=member) & Q(dealstage__name=dealstage))
    else:
        results = Project.objects.filter(Q(dealstage__name=dealstage) & Q(overall_Status__name=ostatus) & Q(member__name=member) & Q(director__name=director)  )

    context = {'project_list':results}
    return render(request, 'projects/search_keyprojects.html' , context = context)

def MyEarlySearch(request):
    member = request.GET.get('mymember')
    stage = request.GET.get('mydirector')
    engagement = request.GET.get('myengagement')
    investor = request.GET.get('myinvestor')

    Projecte = Project.objects.filter(Q(dealstage__name="Early"))
    if (stage == 'any') & (member == 'any') & (engagement == 'any') & (investor == 'any'):
        results = Projecte.all()
    elif (member == 'any') & (engagement == 'any')& (investor == 'any'):
        results = Projecte.filter(director__name=stage)
    elif (stage == 'any') & (engagement == 'any')& (investor == 'any'):
        results = Projecte.filter(member__name=member)
    elif (member == 'any') & (stage == 'any')& (investor == 'any'):
        results = Projecte.filter(engagement__engagement_name=engagement)
    elif (member == 'any') & (engagement == 'any')& (stage == 'any'):
        results = Projecte.filter(sector__name=investor)
    elif (stage == 'any')& (investor == 'any') :
        results = Projecte.filter(engagement__engagement_name=engagement,member__name=member)
    elif (engagement == 'any') & (investor == 'any'):
        results = Projecte.filter(director__name=stage, member__name=member)
    elif (member == 'any')& (investor == 'any'):
        results = Projecte.filter(engagement__engagement_name=engagement, member__name=member)
    elif (stage == 'any')& (engagement == 'any') :
        results = Projecte.filter(sector__name=investor,member__name=member)
    elif (engagement == 'any') & (member == 'any'):
        results = Projecte.filter(director__name=stage,sector__name=investor)
    elif (member == 'any')& (stage == 'any'):
        results = Projecte.filter(engagement__engagement_name=engagement, sector__name=investor)
    elif stage == 'any' :
        results = Projecte.filter(engagement__engagement_name=engagement,member__name=member, sector__name=investor)
    elif engagement == 'any':
        results = Projecte.filter(director__name=stage, member__name=member, sector__name=investor)
    elif member == 'any':
        results = Projecte.filter(engagement__engagement_name=engagement, member__name=member, sector__name=investor)
    elif investor == 'any':
        results = Projecte.filter(engagement__engagement_name=engagement, member__name=member,director__name=stage )
    else:
        results = Projecte.filter(director__name=stage, engagement__engagement_name=engagement,member__name=member,sector__name=investor)

    context = {'project_list':results}
    return render(request, 'projects/search_earlyprojects.html' , context = context)


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

class ProjectnUpdate(UpdateView):
    model = Project
    fields = {'next_step'}

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

class DialougeDelete(DeleteView):
    model = Dialouge
    success_url = reverse_lazy('all_projects')

from .forms import add_doc

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

from .forms import add_dsdate

def ds_new(request):
    if request.method == "POST":
        form = add_dsdate(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_projects')
    else:
        form = add_dsdate()
    return render(request, 'projects/dsdate_form.html', {'form': form})



class PcompaniesCreate(CreateView):
    model = Pcompanies
    fields = '__all__'
    success_url = reverse_lazy('pcompanies_create')

class PcompaniesUpdate(UpdateView):
    model = Pcompanies
    fields = '__all__'
    success_url = reverse_lazy('investor')

class PcompaniesDelete(DeleteView):
    model = Pcompanies
    success_url = reverse_lazy('index')
