from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from login.models import user_details
import datetime
from .models import expert_in,placement_companies,Internship_companies,new_class_placement
from django.contrib.auth import decorators


def index(request):
    
    # user_temp=request.user
    # print(user_temp)
    # return HttpResponse("jenil")
    if request.user.is_authenticated:
        cur_user=request.user
        cur_user_temp=user_details.objects.filter(User=cur_user)[0]
        # print(cur_user_temp.image.url)
        experts=expert_in.objects.filter(user=request.user)
        image=cur_user_temp.image.url
        pass_expert=[]
        for val in experts:
            pass_expert.append(val.exper_field)
        # print(pass_expert)
        name=cur_user_temp.first_name+" "+cur_user_temp.last_name
        cur_sem=cur_user_temp.current_sem
        cgpa=cur_user_temp.cgpa_till_6_sem
        passing={'passing':{'Name':cur_user_temp.first_name+" "+cur_user_temp.last_name,
        'DOB':cur_user_temp.dob,'Semester':cur_user_temp.current_sem,'CGPA':cur_user_temp.cgpa_till_6_sem,'Birth-place':cur_user_temp.Place_of_birth,'Residence':cur_user_temp.homecity},'expert':pass_expert,'image_path':image}
        return render(request,'dashboard/index.html',passing)
    else:
        return HttpResponse("Error 404 Page not found")

def add_skills(request):
    recieved_skill=request.POST['skill']
    confirm_skill=request.POST['conf_skill']
    cur_user=request.user
    skill_is_there=expert_in.objects.filter(user=cur_user)
    ans_flag=False
    for temp_skill in skill_is_there:
        if(str(temp_skill)==str(recieved_skill)):
            ans_flag=True
            break
    if ans_flag==False:
        new_skill_to_add=expert_in(user=cur_user,exper_field=recieved_skill)
        new_skill_to_add.save()        
    
    # print(skill_is_there)
    return redirect("dashboard")

@login_required
def placements(request):
    
    cur_user=request.user
    details=user_details.objects.filter(User=cur_user)[0]
    print(details)
    all_opurtunities=placement_companies.objects.all()
    today=datetime.date.today()
    
    print(type(today))
    
    Internship_companies_avl={}
    Internship_companies_avl['companies']={}
    Internship_companies_avl['user_details']={'cgpa':details.cgpa_till_6_sem}
    i=0
    for temp in all_opurtunities:
        print("Required "+ str(all_opurtunities[i].cgpa_required)+" Your "+ str(details.cgpa_till_6_sem))
        if all_opurtunities[i].available_till>=today and all_opurtunities[i].cgpa_required<=details.cgpa_till_6_sem:
            print("Yes available "+all_opurtunities[i].Company_name)
            company=all_opurtunities[i].Company_name
            role=all_opurtunities[i].Job_role
            cutoff=all_opurtunities[i].cgpa_required
            image_path=all_opurtunities[i].logo.url
            valid_till=all_opurtunities[i].available_till.strftime("%d-%b-%Y")
            stipend=all_opurtunities[i].Salary_offered
            salary_in=all_opurtunities[i].Salary_in
            temp={'image_path':image_path,'Role':role,'Cutoff':cutoff,'Available Till':valid_till,'salary':stipend,'salary_in':salary_in}
            Internship_companies_avl['companies'][company]=temp        
        else:
            print("Expired "+all_opurtunities[i].Company_name)
        i=i+1
        print(Internship_companies_avl)

    
    return render(request,'dashboard/placements.html',Internship_companies_avl)


@login_required
def internships(request):
    cur_user=request.user
    details=user_details.objects.filter(User=cur_user)[0]
    print(details)
    all_opurtunities=Internship_companies.objects.all()
    today=datetime.date.today()
    
    print(type(today))
    print(type(all_opurtunities[0].available_till))
    Internship_companies_avl={}
    Internship_companies_avl['companies']={}
    Internship_companies_avl['user_details']={'cgpa':details.cgpa_till_6_sem}
    i=0
    for temp in all_opurtunities:
        print("Required "+ str(all_opurtunities[i].cgpa_required)+" Your "+ str(details.cgpa_till_6_sem))
        if all_opurtunities[i].available_till>=today and all_opurtunities[i].cgpa_required<=details.cgpa_till_6_sem:
            print("Yes available "+all_opurtunities[i].Company_name)
            company=all_opurtunities[i].Company_name
            role=all_opurtunities[i].Job_role
            cutoff=all_opurtunities[i].cgpa_required
            image_path=all_opurtunities[i].logo.url
            valid_till=all_opurtunities[i].available_till.strftime("%d-%b-%Y")
            stipend=all_opurtunities[i].Salary_offered
            salary_in=all_opurtunities[i].Salary_in
            temp={'image_path':image_path,'Role':role,'Cutoff':cutoff,'Available Till':valid_till,'salary':stipend,'salary_in':salary_in}
            Internship_companies_avl['companies'][company]=temp        
        else:
            print("Expired "+all_opurtunities[i].Company_name)
        i=i+1
        print(Internship_companies_avl)

    
    return render(request,'dashboard/internship.html',Internship_companies_avl)

def offers(request):

    cur_user=request.user
    all_offers=new_class_placement.objects.filter(user=cur_user)
    all_offers.reverse()
    print(all_offers)
    dict_to_pass={}
    dict_to_pass['companies']={}
    i=0
    for offer in all_offers:
        message=all_offers[i].message
        company=all_offers[i].offer_id.Company_name
        stipend=all_offers[i].stipend
        position=all_offers[i].offer_id.Job_role
        salary_in=all_offers[i].offer_id.Salary_in
        img_url=all_offers[i].offer_id.logo.url
        temp={'message':message,'salary':stipend,'position':position,'salary_in':salary_in,'img_path':img_url}
        dict_to_pass['companies'][company]=temp
        i=i+1
    return render(request,'dashboard/offers.html',dict_to_pass)