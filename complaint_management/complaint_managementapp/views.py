from django.shortcuts import render, redirect
from complaint_managementapp.models import Contact, Customer, Administration, AddCatagory, Solvers, Update_Status, \
    Send_Query, Replay

from complaint_managementapp.forms import ContactForm, CustomerForm, AdministrationForm, AddCatagoryForm, SolversForm, \
    Update_StatusForm, Send_QueryForm, ReplayForm


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def blog(request):
    return render(request, "blog.html", {})


def blog_single(request):
    return render(request, "blog_single.html", {})


def main(request):
    return render(request, "main.html", {})


def rooms(request):
    return render(request, "rooms.html", {})


def services(request):
    return render(request, "services.html", {})


def contact(request):
    if request.method == "POST":
        print("hii")
        form = ContactForm(request.POST)
        print("hii")
        if form.is_valid():
            print("hello")
            print("hloo")
            form.save()
        return render(request, "contact.html", {"msg": "success"})
    return render(request, "contact.html", {})


# Customer Views
def customer(request):
    return render(request, "customer_login.html", {})


def regpage(request):
    return render(request, "customer_reg.html", {})


def customer_reg(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        print(form.errors)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(e)
    return render(request, "customer_login.html", {"msg": ""})


def is_customer_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def customer_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        customer = Customer.objects.filter(email=email, password=password)
        if customer.exists():
            request.session["email"] = email
            return render(request, "customer.html", {"msg": email})
        else:
            return render(request, "customer_login.html", {"msg": "email or password not exist"})
    return render(request, "customer_login.html", {"msg": ""})


def customer_home(request):
    return render(request, "customer.html", {})


def customer_change(request):
    if is_customer_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]

            try:
                customer = Customer.objects.get(email=email, password=password)
                customer.password = newpassword
                customer.save()
                msg = "password updated successfully"
                return render(request, "customer_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "customer_change.html", {"msg": msg})
        return render(request, "customer_change.html", {})
    else:
        return render(request, "customer_change.html", {})


def customer_display(request):
    customer = Customer.objects.all()
    print("hello")
    return render(request, "customer_display.html", {"customer": customer})


def customer_delete(requedef, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/customer_reg")


def customer_edit(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, "customer_edit.html", {"customer": customer})
    # if customer.is_valid():
    #     customer.save()
    # return redirect("/customer_display")


def addcatagory(request):
    if request.method == "POST":
        addcatagory = AddCatagoryForm(request.POST, request.FILES)
        if addcatagory.is_valid():
            addcatagory.save()
        return render(request, "addcatagory.html", {"msg": "success"})
    return render(request, "addcatagory.html", {})


def addcatagory_delete(request, id):
    addcatagory = AddCatagory.objects.get(id=id)
    addcatagory.delete()
    return redirect("/addcatagory")


def addcatagory_edit(request, id):
    addcatagory = AddCatagory.objects.get(id=id)
    return render(request, "addcatagory_edit.html", {"addcatagory": addcatagory})


def customer_update(request):
    if request.method == "POST":
        customerid = request.POST["id"]
        customer = Customer.objects.get(id=customerid)
        customer = CustomerForm(request.POST, instance=customer)
        if customer.is_valid():
            customer.save()
        return redirect("/customer_display")
    return redirect("/customer_display")


def addcatagory_update(request):
    if request.method == "POST":
        addcatagoryid = request.POST["id"]
        addcatagory = AddCatagory.objects.get(id=addcatagoryid)
        addcatagory = AddCatagoryForm(request.POST, instance=addcatagory)
        if addcatagory.is_valid():
            addcatagory.save()
        return redirect("/customer_viewcatagory")
    return redirect("/customer_viewcatagory")


def accept_addcatagory(request, id):
    accept = AddCatagory.objects.get(id=id)
    accept.status = 1
    accept.save()
    return redirect("/admin_viewcatagory")


def reject_addcatagory(request, id):
    reject = AddCatagory.objects.get(id=id)
    reject.status = 2
    reject.save()
    return redirect("/admin_viewcatagory")


def cancel_addcatagory(request, id):
    reject = AddCatagory.objects.get(id=id)
    reject.status = 3
    reject.save()
    return render(request, "customerview_catagory.html", {})


def customer_viewcatagory(request):
    addcatagory = AddCatagory.objects.all()
    print("hi")
    return render(request, "customer_viewcatagory.html", {"addcatagory": addcatagory})


def customer_send_query(request):
    if request.method == "POST":

        send_query = Send_QueryForm(request.POST)
        if send_query.is_valid():
            send_query.save()
        return render(request, "customer_send_query.html", {"msg": "success"})
    solvers = Solvers.objects.all()
    return render(request, "customer_send_query.html", {"solvers": solvers})


def view_update_status(request):
    update_status = Update_Status.objects.all()
    print("hello")
    return render(request, "view_update_status.html", {"update_status": update_status})


def customer_view_replay(request, id):
    solvers = Solvers.objects.get(id=id)
    replay = Replay.objects.filter(solvers_id=solvers.id)
    print("hello")
    return render(request, "customer_view_replay.html", {"replay": replay})


def customer_view_query(request):
    send_query = Send_Query.objects.all()
    print("hello")
    return render(request, "customer_view_query.html", {"send_query": send_query})


def solvers_view_query(request):
    send_query = Send_Query.objects.all()
    print("hello")
    return render(request, "solvers_view_query.html", {"send_query": send_query})


def customer_logout(request):
    if request.session.has_key("email"):
        email = request.session["email"]
        return render(request, "customer_login.html", {"email": email})


# Admin Views
def administration(request):
    return render(request, "admin_login.html", {})


def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        administration = Administration.objects.filter(email=email, password=password)
        if administration.exists():
            print("hello")
            request.session["email"] = email
            return render(request, "administration.html", {"msg": email})
        else:
            return render(request, "admin_login.html", {"msg": "email or password not exist"})
    return render(request, "admin_login.html", {"msg": ""})


def admin_home(request):
    return render(request, "administration.html", {})


def is_admin_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def admin_change(request):
    if is_admin_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]

            try:
                administration = Administration.objects.get(email=email, password=password)
                administration.password = newpassword
                administration.save()
                msg = "password updated successfully"
                return render(request, "admin_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "admin_change.html", {"msg": msg})
        return render(request, "admin_change.html", {})
    else:
        return render(request, "admin_change.html", {})


def admin_logout(request):
    if request.session.has_key("email"):
        email = request.session["email"]
        return render(request, "admin_login.html", {"email": email})


def update_status(request, id):
    addcatagory = AddCatagory.objects.get(id=id)
    if request.method == "POST":
        form = Update_StatusForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "update_status.html", {"msg": "success", "addcatagory": addcatagory.id})

    return render(request, "update_status.html", {"addcatagory": addcatagory.id})


def admin_viewcustomer(request):
    customer = Customer.objects.all()
    print("hello")
    return render(request, "admin_viewcustomer.html", {"customer": customer})


def admin_viewcontact(request):
    contact = Contact.objects.all()
    print("hello")
    return render(request, "admin_viewcontact.html", {"contact": contact})


def admin_viewquery(request):
    send_query = Send_Query.objects.all()
    print("hello")
    return render(request, "admin_view_query.html", {"send_query": send_query})


def admin_viewcatagory(request):
    addcatagory = AddCatagory.objects.all()
    print("hello")
    return render(request, "admin_view_catagory.html", {"addcatagory": addcatagory})


# manager views
def solvers(request):
    return render(request, "solvers_login.html", {})


def solvers_regpage(request):
    return render(request, "solvers_reg.html", {})


def solvers_reg(request):
    if request.method == "POST":
        form = SolversForm(request.POST)
        print(form.errors)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(e)
    return render(request, "solvers_login.html", {"msg": ""})


def solvers_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        solvers = Solvers.objects.filter(email=email, password=password)
        if solvers.exists():
            request.session["email"] = email
            return render(request, "solvers.html", {"msg": email})
        else:
            return render(request, "solvers_login.html", {"msg": "email or password not exist"})
    return render(request, "solvers_login.html", {})


def solver_home(request):
    return render(request, "solvers.html", {})


def is_solvers_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def solvers_change(request):
    if is_solvers_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]

            try:
                solvers = Solvers.objects.get(email=email, password=password)
                solvers.password = newpassword
                solvers.save()
                msg = "password updated successfully"
                return render(request, "solvers_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "solvers_change.html", {"msg": msg})
        return render(request, "solvers_change.html", {})
    else:
        return render(request, "solvers_change.html", {})


def solvers_display(request):
    solvers = Solvers.objects.all()
    print("hello")
    return render(request, "solvers_display.html", {"solvers": solvers})


def solvers_edit(request, id):
    solvers = Solvers.objects.get(id=id)
    return render(request, "solvers_edit.html", {"solvers": solvers})


def solvers_update(request):
    if request.method == "POST":
        solversid = request.POST["id"]
        solvers = Solvers.objects.get(id=solversid)
        solvers = SolversForm(request.POST, instance=solvers)
        if solvers.is_valid():
            solvers.save()
        return redirect("/solvers_display")
    return redirect("/solvers_display")


def solvers_delete(request, id):
    solvers = Solvers.objects.get(id=id)
    solvers.delete()
    return redirect("/solvers_reg")


def solvers_view_query(request):
    send_query = Send_Query.objects.all()
    print("hello")
    return render(request, "solvers_view_query.html", {"send_query": send_query})


def solvers_replay(request, id):
    solvers = Solvers.objects.get(id=id)
    if request.method == "POST":
        replay = ReplayForm(request.POST)
        if replay.is_valid():
            print("errors", replay.errors)
            replay.save()
        return render(request, "solvers_replay.html", {"msg": "success", "solvers": solvers.id})
    return render(request, "solvers_replay.html", {"solvers": solvers.id})


def solvers_logout(request):
    if request.session.has_key("email"):
        email = request.session["email"]
        return render(request, "solvers_login.html", {"email": email})
