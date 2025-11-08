from datetime import datetime
import random
from django.shortcuts import render, redirect

gold_map={
    "farm" :(10,20),
    "cave" :(5, 10),
    "house": (2, 5),
    "casino": (-50, 50),
}

def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
        request.session["activities"] = []
    context = {
        "gold": request.session["gold"],
        "activities": request.session["activities"],
    }
    return render(request, "index.html", context)
 
def process_money(request):
    if request.method == "POST":
        building = request.POST.get("building")
        if building in gold_map:
            min_gold, max_gold = gold_map[building]
            earned = random.randint(min_gold, max_gold)
            request.session["gold"] += earned

            currentTime = datetime.now().strftime("%Y/%m/%d %I:%M %p")
            if earned >= 0:
                color = "green"
                message = f"Earned {earned} golds from the {building}! ({currentTime})"
            else:
                color = "red"
                message = f"Entered a {building} and lost {abs(earned)} golds... Ouch! ({currentTime})"

            activities = request.session["activities"]
            activities.insert(0, {"message": message, "color": color})
            request.session["activities"] = activities
    return redirect("/")

def reset(request):
    request.session.flush()
    return redirect("/")