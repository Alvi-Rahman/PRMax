from django.shortcuts import render


def home_page(request):
    if request.method == "GET":
        return render(request, template_name="home_page.html", context={"get": True})
    elif request.method == "POST":

        if request.POST["age"] is not None and int(request.POST["age"]) < 18:
            code = "A"
        else:
            code = "B"

        return render(request, template_name="home_page.html",
                      context={
                          "first_name": request.POST["first_name"],
                          "last_name": request.POST["last_name"],
                          "age": request.POST["age"],
                          "address": request.POST["address"],
                          "email": request.POST["email"],
                          "code": code,
                          "get": False,
                      }
                      )
